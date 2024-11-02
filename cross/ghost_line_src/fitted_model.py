
def calculate_model(AD, D1, D2, OC, skew):
    """
    The model only include the terms that have p-value < 0.05 from a full model of all the evaluation values
    
    +-----------------------------------------------------+-----------+
    | Term                                                | Estimate  |
    +-----------------------------------------------------+-----------+
    | Intercept                                           | 1.8474584 |
    | AD                                                  | -0.089558 |
    | D1                                                  | 0.9231891 |
    | (AD-8.72075)*(D1-0.275)                             | -0.145991 |
    | D2                                                  | 0.5767543 |
    | (AD-8.72075)*(D1-0.275)*(D2-0.48958)                | 0.2355008 |
    | (skew-0.15617)*(D1-0.275)*(D2-0.48958)              | 6.5093376 |
    | (AD-8.72075)*(skew-0.15617)*(D1-0.275)*(D2-0.48958) | -1.196248 |
    | OC                                                  | 0.4846924 |
    | (D1-0.275)*(OC-1.13154)                             | -0.505861 |
    | (AD-8.72075)*(skew-0.15617)*(D1-0.275)*(OC-1.13154) | 0.5910252 |
    +-----------------------------------------------------+-----------+

    Args:
        AD: the mean of four cross-sections of AD-value from Anderson Darling normality test
        D1: the mean of four cross-sections of first derivative tests 
        D2: the mean of four cross-sections of second derivative tests 
        OC: the mean of four cross-sections of off center values
        skew: the mean of four cross-sections of skewness
        
    Returns:
        a float number of the model estimated response

    """
    # Define the coefficients
    coefficients = [
        1.8474584,
        -0.089558,
        0.9231891,
        -0.145991,
        0.5767543,
        0.2355008,
        6.5093376,
        -1.196248,
        0.4846924,
        -0.505861,
        0.5910252
    ]

    # Define the mean values used in the model
    AD_mean = 8.72075
    D1_mean = 0.275
    D2_mean = 0.48958
    skew_mean = 0.15617
    OC_mean = 1.13154

    # Calculate each term
    terms = [
        1,  # Intercept
        AD,
        D1,
        (AD - AD_mean) * (D1 - D1_mean),
        D2,
        (AD - AD_mean) * (D1 - D1_mean) * (D2 - D2_mean),
        (skew - skew_mean) * (D1 - D1_mean) * (D2 - D2_mean),
        (AD - AD_mean) * (skew - skew_mean) * (D1 - D1_mean) * (D2 - D2_mean),
        OC,
        (D1 - D1_mean) * (OC - OC_mean),
        (AD - AD_mean) * (skew - skew_mean) * (D1 - D1_mean) * (OC - OC_mean)
    ]

    # Calculate the result
    result = sum(coef * term for coef, term in zip(coefficients, terms))

    return result

