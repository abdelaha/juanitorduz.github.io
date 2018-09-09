---
Title: Circle Fit
Date: 2018-09-09
Category: R
Tags: r_notebook, r, geometry
slug: circle_fit
Authors: Juan Camilo Orduz
Summary: We explore how to include an R notebook into a pelican post. As an example, we describe how to fit a circle onto a cloud of points. 
---

In view of the [R Kernel Jupyter Notebook](https://juanitorduz.github.io/rkernel.html) post, I wanted to explore how to include an [R Notebook](https://bookdown.org/yihui/rmarkdown/notebook.html) directly into [Pelican](https://blog.getpelican.com). Fortunately, I found a great [post](http://michaeltoth.me/how-to-write-pelican-blog-posts-using-rmarkdown-knitr-20.html) where an R function is provided in order to render R Notebooks into Pelican format. Works great! 

To play around with it, I wrote a simple R notebook which fits a circle to a cloud of points. 

# Prepare the Notebook


```r
library(tidyverse)
```

# Generate Circle Data


```r
# Dimension of the space.
d <- 2

# Number of sample points. 
N <- 1000

# Radius. 
R <- 4

# Generate random sample of points (x - axis).
points.0 <- 1:N %>% map(.f = function(x) runif(n = d - 1, min =  - R, max = R))

# Generate the corresponding y - coordinates. 
all.points <- points.0 %>% map(.f = function(x) c(x, sign(runif(n = 1, min = - 1, max = 1))*sqrt(R^2 - norm(x, type = '2')^2))) 

# Store data in a tibble.
all.points.df <- all.points %>% reduce(.f = function(x, y) rbind(x, y)) %>% 
                                as.tibble %>% 
                                rename(x = V1, y = V2)

# Plot the data. 
all.points.df %>% ggplot() + theme_light() + geom_point(mapping = aes(x = x, y = y)) 
```

![center](/images/r_circle_fit/unnamed-chunk-2-1.png)

# Add Noise 

We add noise from a normal disttribution with mean zero and standard deviation `sd`.


```r
# Set standard deviation.
sd <- 0.5

# Add noise.
all.samples <- all.points %>% map(.f = function(x) x + rnorm(n = d, mean = 0, sd = sd))

# Store data in a tibble.
all.samples.df <- all.samples %>% reduce(.f = function(x, y) rbind(x, y)) %>%
                                  as.tibble %>% 
                                  rename(x = V1, y = V2)

# Plot the data.
all.samples.df %>% ggplot() + theme_light() + geom_point(mapping = aes(x = x, y = y)) 
```

![center](/images/r_circle_fit/unnamed-chunk-3-1.png)

# Define Optimization Function

In order to find the best fitting circle, we need to define what "best" means. We aim to minimize the RMSE. 


```r
# Define function to optimize. 
ComputeRMSE <- function(all.samples, r, N) {
  
  all.samples %>% map_dbl(.f = function(x) (r - norm(x, type = '2'))^2) %>% mean
  
}
```

Let us visualize the shape of the cost function. 


```r
rmse.df <- seq(from = 0.5, to = 10, by = 0.1) %>% 
              map(.f = function(r) c(r, ComputeRMSE(all.samples = all.samples, r = r, N = N ))) %>% 
              reduce(.f = function(x, y) rbind(x, y)) %>% 
              as.tibble %>% 
              rename(r = V1, RMSE = V2)

rmse.df %>% ggplot() + theme_light() + geom_line(mapping = aes(x = r, y = RMSE))
```

![center](/images/r_circle_fit/unnamed-chunk-5-1.png)

We aim to find the minimum. 

# Run Optimization


```r
opt.obj <- optimize(f =function(r) ComputeRMSE(all.samples = all.samples, r = r, N = N), interval = 1:10)

r.hat <- opt.obj$minimum

r.hat
```

```
## [1] 4.05987
```

# Visualize Results 

We project each sample point onto the best circle fit. 


```r
all.samples %>% map(.f = function(x) r.hat*x /norm(x, type = '2')) %>% 
                reduce(.f = function(x, y) rbind(x, y)) %>% 
                as.tibble %>% 
                rename(x1 = V1, y1 =V2) %>% 
                cbind(all.samples.df) %>% 
                ggplot() + 
                theme_light() + 
                geom_point(mapping = aes(x = x, y = y)) +
                geom_point(mapping = aes(x = x1, y = y1), color = 'red') 
```

![center](/images/r_circle_fit/unnamed-chunk-7-1.png)

# Analytical Solution 

By taking the derivative of the cost function with respect to `r` we can easily get the value of `r.hat`.


```r
r.hat <- all.samples %>% map_dbl(.f = function(x) norm(x, type = '2')) %>% mean

r.hat
```

```
## [1] 4.05987
```

