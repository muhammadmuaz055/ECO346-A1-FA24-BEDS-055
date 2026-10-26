# Q4: R's untouched defaults. Nothing added to ggplot() + geom_point().
source("scripts/00_common.R")
p <- ggplot(earners, aes(age, earn_annual)) + geom_point()
ggsave("figures/default.svg", p, width = 7, height = 5)
