xs <- 0:200/10
plot(NA, NA, xlim = c(0, 20), ylim = c(0, 50))
for (k in 1:10) {
  lines(xs, k * sqrt(xs) - xs)  
}
