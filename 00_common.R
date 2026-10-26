# Shared set-up, sourced by scripts 01-03. Run all scripts from the repository root.
suppressPackageStartupMessages({
  library(dplyr); library(readr); library(ggplot2); library(scales); library(svglite)
})
dir.create("figures", showWarnings = FALSE); dir.create("tables", showWarnings = FALSE)

PROV <- 4; AREA <- 2   # variant 7 = Balochistan urban (edit for your variant)

persons <- read_csv("data/pslm_person_subset.csv", col_select = c(hhid, age, earn_annual), show_col_types = FALSE)
hh      <- read_csv("data/pslm_hh_subset.csv", col_select = c(hhid, hhweight, prov_code, urban_rural), show_col_types = FALSE)

earners <- persons |>
  left_join(hh, by = "hhid") |>
  filter(prov_code == PROV, urban_rural == AREA, age >= 15, age <= 64, earn_annual > 0)

w_mean <- function(x, w) sum(w * x) / sum(w)

# Weighted quantile exactly as defined in the brief (NOT quantile())
w_quantile <- function(x, w, p) {
  o <- order(x); x <- x[o]; w <- w[o]
  cw <- cumsum(w) / sum(w)
  x[which(cw >= p - 1e-12)[1]]
}

rupee_breaks <- 10^(4:7)
rupee_labels <- c("Rs 10,000", "Rs 100,000", "Rs 1,000,000", "Rs 10,000,000")
