library(shiny)

## Cards

c_give_up <- list(name = "Give up",
                  desc = "reset ranks, +5 en to both",
                 lg = function(cur, opp) TRUE,
                 fx = function(cur, opp) {
                   cur$rk <- 0
                   opp$rk <- 0
                   cur$en <- cur$en + 5
                   opp$en <- opp$en + 5                   
                   list(cur = cur, opp = opp)
                 })

c_energy_1 <- list(name = "Energy 1",
                   desc = "-1 PTS, convert PTS to EN",
                 lg = function(cur, opp) cur$pts > 0,
                 fx = function(cur, opp) {
                   cur$pts <- cur$pts - 1
                   cur$en <- cur$en + cur$pts
                   cur$pts <- 0
                   list(cur = cur, opp = opp)
                 })

cards <- list(c_give_up, c_energy_1)

for (i in 1:11) {
  rk <- i
  en <- 2 * i
  pts <-  floor(5 * sqrt(i))
  cards <- c(cards, 
             list(list(name = paste("Points", i),
                       desc = paste0("rank:", rk, ", -", en, " EN, + ", pts, " PTS"),
                  rk = rk,
                  en = en,
                  pts = pts
             )))
}

nchoices <- as.list(1:length(cards)); names(nchoices) <- sapply(cards, function(v) {
  paste0(v$name, " (", v$desc, ")")
  })

play_card <- function(num, cur, opp) {
  card <- cards[[num]]
  if (!is.null(card$lg)) {
    legal <- card$lg(cur, opp)
  } else {
    legal <- (card$rk > opp$rk) & (card$en <= cur$en)
  }
  if (legal) {
    if (!is.null(card$fx)) {
      res <- card$fx(cur, opp)
      cur <- res$cur
      opp <- res$opp
    } else {
      cur$pts <- cur$pts + card$pts
      cur$en <- cur$en - card$en
      cur$rk <- card$rk
    }
  }
  list(legal = legal, cur = cur, opp = opp)
}

update_state <- function(num) {
  if (turn_no %% 2 == 0) {
    cur <- game_state$p2
    opp <- game_state$p1    
  } else {
    cur <- game_state$p1
    opp <- game_state$p2    
  }
  res <- play_card(num, cur, opp)
  if (turn_no %% 2 == 0) {
    game_state$p2 <<- res$cur
    game_state$p1 <<- res$opp
  } else {
    game_state$p1 <<- res$cur
    game_state$p2 <<- res$opp
  }
  if (res$legal == TRUE) turn_no <<- turn_no + 1  
}

display_state <- function() {
  tab <- matrix(0, 2, 3)
  rownames(tab) <- c("Player A", "Player B")
  colnames(tab) <- c("energy (EN)", "points (PTS)", "rank")
  for (i in 1:2) {for (j in 1:3) {
    tab[i, j] <- game_state[[i]][[j]]    
  }}
  tab
}

get_current_player <- function() {
  if (turn_no %% 2 == 0) {
    return("Player B")
  }
  "Player A"
}

ui = shinyUI(
  fluidPage(
    fluidRow(actionButton("quitApp", label = "Close")),
    fluidRow(
      uiOutput("dynamicOutput")
    ),
    fluidRow(column(1, actionButton("ch", label = "Choose"))),
    fluidRow(
      uiOutput("dynamicDisplay")
    ),
    fluidRow(column(1, actionButton("rf", label = "Refresh")))
  )
)

server = function(input, output) {
  observe({
    if (input$quitApp == 1) {
      stopApp()
    }
    if (input$ch > 0) {
      isolate({
        print(input$num)
        update_state(as.numeric(input$num))
      })
    }
  })
  output$dynamicOutput <- renderUI({
    input$ch
    radioButtons(
      "num",
      label = get_current_player(),
      choices = nchoices
    )
  })
  output$dynamicDisplay <- renderTable({
    input$num
    isolate({
      display_state()
    })
  })
}

p1state <- list("en" = 30, "pts" = 0, "rk" = 0)
p2state <- list("en" = 30, "pts" = 0, "rk" = 0)
game_state <- list("p1" = p1state, "p2" = p2state)
turn_no <- 1
runApp(list(ui = ui, server = server))