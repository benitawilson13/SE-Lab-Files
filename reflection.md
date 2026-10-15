# Lab 5 – Static Code Analysis Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were unused imports, missing newlines, and incorrect comparisons with `None`. These required only small changes to the code. The hardest issues were security-related problems, such as using `eval()`, weak MD5 hashing, and generating booking PINs using the normal `random` module. These required understanding the security risks and replacing the unsafe code with safer alternatives.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

During this lab, I did not identify any clear false positives. Most warnings reported by Pylint, Bandit, and Flake8 were valid issues in the original code. For example, Flake8 reported an unused `math` import, and Pylint identified an unused variable. These warnings helped improve code cleanliness and readability. Static analysis results should still be reviewed because tools may sometimes report warnings that are not actual problems in a particular context.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run static analysis tools regularly while developing software. I would use Flake8 to identify style and formatting issues, Pylint to check code quality and maintainability, and Bandit to detect potential security vulnerabilities. I would run these tools before committing code to GitHub and include them in a CI/CD pipeline so that issues can be detected automatically. This would help maintain code quality and reduce errors early in development.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes, the code became cleaner, more readable, and more secure. I removed unused imports and variables, improved exception handling, corrected comparisons, and added appropriate documentation. I also replaced unsafe `eval()` usage, weak MD5 hashing, and predictable PIN generation with safer alternatives. The final Pylint score improved to 10.00/10, Bandit reported no issues, and Flake8 produced no errors. These results indicate improved code quality and reduced potential security risks.