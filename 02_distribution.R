# Q2: weighted histogram of log10 annual earnings.
source("scripts/00_common.R")
x <- earners$earn_annual; w <- earners$hhweight
n_earners <- nrow(earners)
w_med <- w_quantile(x, w, 0.5); u_med <- median(x)
p10 <- w_quantile(x, w, 0.1);   p90 <- w_quantile(x, w, 0.9)
excluded <- sum(x < 1e4 | x > 1e7)
cat(sprintf("earners=%d | weighted median=%s | unweighted median=%s | p10=%s | p90=%s | p90/p10=%.2f | excluded=%d\n",
            n_earners, comma(w_med), comma(u_med), comma(p10), comma(p90), p90 / p10, excluded))

d <- earners |> filter(earn_annual >= 1e4, earn_annual <= 1e7) |> mutate(lx = log10(earn_annual))
p <- ggplot(d, aes(lx, weight = hhweight)) +
  geom_histogram(aes(y = after_stat(density)), breaks = seq(4, 7, by = 0.1),
                 fill = "#4C78A8", colour = "white") +
  geom_vline(xintercept = log10(c(w_med, p90)), linetype = "dashed") +
  annotate("text", x = log10(w_med), y = Inf, label = paste0("Median\nRs ", comma(w_med)),
           hjust = 1.08, vjust = 1.3, size = 3.4) +
  annotate("text", x = log10(p90), y = Inf, label = paste0("90th pct\nRs ", comma(p90)),
           hjust = -0.08, vjust = 1.3, size = 3.4) +
  scale_x_continuous(breaks = 4:7, labels = rupee_labels, limits = c(4, 7)) +
  labs(title = "Urban Balochistan earnings are right-skewed: the top tenth earn over 5 times the bottom tenth",
       x = "Annual earnings (log scale)", y = "Density per log10 unit",
       caption = paste0("Source: PSLM 2019-20 person file. Sample: earners aged 15-64, Balochistan urban (n = ", n_earners,
                        "). Weighted by hhweight. Earners outside Rs 10,000-10,000,000 excluded: ", excluded, ".")) +
  theme_minimal(base_size = 11) +
  theme(plot.title = element_text(face = "bold", size = 11), plot.caption = element_text(size = 7, hjust = 0))
ggsave("figures/fig_02_distribution.svg", p, width = 8, height = 5)
