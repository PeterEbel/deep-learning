### Estimated population variance

The estimated population variance is typically calculated using sample data. It's an estimate of the population variance based on information obtained from a sample of the population. The formula for estimating the population variance from sample data is as follows:

$
\begin{aligned}
&\Large s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2 \\
\end{aligned}
$

Where:
- $n$ is the size of the sample (the number of observations in the sample).
- $x_i$ represents each individual value in the sample.
- $\bar{x}$ is the sample mean (average).

This formula is similar to the one for calculating the population variance, but it uses the sample mean $\bar{x}$ instead of the population mean $\mu$, and it divides by $n-1$ instead of $N$ to account for the degrees of freedom in the sample.

After calculating the estimated population variance $s^2$, the estimated population standard deviation $s$ can be found by taking the square root of the estimated population variance.

$
\begin{aligned}
&\Large s = \sqrt{s^2} \\
\end{aligned}
$

It's important to note that because the estimated population variance and standard deviation are based on sample data, they are estimates of the true population parameters and may not be exactly equal to the population variance and standard deviation. However, as the sample size increases, these estimates tend to get closer to the true population parameters.

In statistics, the concept of degrees of freedom refers to the number of independent pieces of information available in a dataset that are free to vary. When we calculate the sample variance, we are using the sample mean ($\bar{x}$) as an estimate of the population mean ($\mu$). However, once the sample mean is calculated, the remaining data points have less freedom to vary. Specifically, if we know the mean of a set of data, we can determine all but one of the data points and the last data point will be determined by the requirement that the sum of all data points equals the mean times the number of data points. 

For example, if we have a sample of 5 numbers and we know the mean is 10, and we know 4 of the numbers are 8, 9, 11, and 12, then the last number must be 10, in order to ensure that the mean of the sample remains 10. So, out of the $n$ data points in the sample, once the sample mean is known, only $n-1$ of them are free to vary independently. This is why we divide by $n-1$ rather than $n$ when calculating the sample variance. By dividing by $n-1$ instead of $n$, we're adjusting for this loss of freedom in the sample, allowing the sample variance to provide a better estimate of the population variance. This adjustment accounts for the fact that we're using the sample mean, rather than the true population mean, in our calculations.