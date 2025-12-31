In this document, we show you how to manually generate/edit a `.zip` file for an omegaUp problem. This document is intended for more experienced users or those who require more specific functionalities (e.g., Karel problems). If you're just starting to write problems or have simpler needs, we recommend using the [Problem Creator](https://mau-md.github.io/Omegaup-CDP/#/) and watching this [tutorial](https://www.youtube.com/watch?v=cUUP9DqQ1Vg&list=PL43fZBs80z1OdkZqSZte3vXA-8VKyh_ZZ&index=2&t=329s) on how to use it.

If you chose the manual option described in this document, we also recommend watching [part 1](https://www.youtube.com/watch?v=LfyRSsgrvNc) and [part 2](https://www.youtube.com/watch?v=i2aqXXOW5ic) of the tutorial on how to manually create problems for omegaUp.

# Configuration

omegaUp problems have several configurable variables:

* **Validator**:
    * **Token by token**: Reads all tokens (sequences of up to 4,194,304 printable contiguous characters separated by spaces) from the expected output file and the user's output, and validates that both sequences are identical.
    * **Token by token, ignoring case**: Same as above, but converts all tokens to lowercase before comparison.
    * **Numeric tokens with 1e-9 tolerance**: Reads numeric tokens (contiguous sequences of numbers and decimal separators), interprets them as numbers, and checks that both sequences have the same length and their corresponding values differ by no more than 1e-9 absolute or relative error.
    * **Interpret stdout as score**: Reads standard output, converts it to a float number, restricts it to the range [0.0, 1.0], and uses it as the final score. Mostly used for interactive problems to avoid cheating.
    * **Custom validator (`validator.$lang$`)**: Allows a custom program that reads the contestant's stdout (and both the input and expected output files), and prints a float in [0.0, 1.0]. See the [validator.$lang$ (optional)](#validatorlang-optional) section for implementation.

* **Languages**:
    * **C, C++, etc.**: Contestants can submit source code in supported languages.
    * **Karel**: Contestants can submit source code in Karel.
    * **Output only**: Contestants submit a `.zip` file with answers for all cases. To allow single case submission as plain text, there must be only one case named `Main.in`/`Main.out`.
    * **No submissions**: Contestants cannot submit. Used only for displaying content in courses.

* **Validator time limit (ms)**: Max real time in milliseconds the grader waits for the validator to return a verdict per case before returning `JE`.
* **Time limit (ms)**: Max CPU time in milliseconds the contestant's program is allowed per case before it's killed with `TLE`.
* **Total time limit (ms)**: Max real time the grader waits for the entire problem to execute before returning `TLE`. Cases are evaluated lexicographically.
* **Extra time for libinteractive (ms)**: Max real time for the judge's program per case before it's terminated with `TLE`.
* **Memory limit (KiB)**: Max RAM (heap+stack) in kibibytes the program can use before being terminated with `MLE`.
* **Output limit (bytes)**: Max bytes a program can write to stdout/stderr before being terminated with `OLE`. This is auto-detected from `.out` file sizes plus 10KiB, unless a custom validator is used.
* **Input limit (bytes)**: Max byte size of the contestant's program. Use to avoid hardcoded/precomputed solutions.
* **Source**: Attribution or origin of the problem.
* **Public listing**: Whether the problem appears in public listings and is available for contests and courses.
* **Send clarifications via email**: Whether omegaUp can email the problem author when users request clarifications.
* **Tags**: Classification tags for the problem.

# Language Problems (C/C++/Java/Pascal)

To upload a problem to omegaUp, you need to save everything inside a **.ZIP** file (not `.rar`, `.tar.bz2`, `.7z`, `.zx`). The zip filename doesn't matter.

The zip must contain the following elements:

### cases/

* This folder should contain all the test cases with `.in` and `.out` extensions. Filenames don't matter, but names must be matched, e.g., `1.in 1.out`, `hello.in hello.out`.

* **Do not use `.` in case names unless you're grouping cases:**

* omegaUp supports grouped cases, meaning you must solve all cases in a group to earn points. Useful when possible outputs are limited. To group, separate the group and case name with a `.`. Example: `group1.case1.in group1.case1.out`, `group1.case2.in group1.case2.out`.

* No limit on the number of cases, but recommended total case size is under 100MB.

* More cases means longer grading time per submission and may delay contests, especially if a solution causes `TLE`.

### statements/

* Must contain the problem statement in Markdown format (`es.markdown`). Use [https://omegaup.com/redaccion.php](https://omegaup.com/redaccion.php) to preview formatting.

* Full LaTeX support. Examples at [http://www.thestudentroom.co.uk/wiki/LaTex](http://www.thestudentroom.co.uk/wiki/LaTex).

* For a better contestant experience, make sure the preview looks good, including input/output tables.

* Wrap variable names like `$n$`, `$x$` to highlight them. Use `$x_i$` for subscripts.

### solutions/

* Similar to **statements/**. Contains the problem solution in markdown format. Must be named `es.markdown`, with optional translations: `en.markdown`, `pt.markdown`.

* Examples of problem files can be found [here](https://github.com/omegaup/omegaup/tree/master/frontend/tests/resources), especially [testproblem.zip](https://github.com/omegaup/omegaup/blob/master/frontend/tests/resources/testproblem.zip) which contains solutions.

### interactive/ (optional)

* Interactive problems must be created using [libinteractive](https://omegaup.com/libinteractive/). See that page for more info.

* For a reference structure, use [Cave from IOI 2013](https://omegaup.com/resources/cave.zip).

### validator.$lang$ (optional)

* If a custom validator is needed, include a file `validator.$lang$` in the root of the zip, where `$lang$` is one of `c`, `cpp`, `java`, `p` (Pascal), or `py`. Only one validator is needed and it's language-independent from the contestant's submission.

* In the validator, you can open `data.in` (same as the input given to the contestant). The validator receives the contestant's output via standard input.

* It's equivalent to running: `./contestant < data.in | ./validator casebasename`, where `casebasename` is the `.in` filename without extension.

* You may also open `data.out`, which is the expected output for the current case.

* The validator **must** output a float between 0 and 1 to stdout indicating the percentage correctness. If nothing is printed, it results in `JE`. Less than 0 becomes 0; more than 1 becomes 1.

* Validators also run in the same sandbox as contestant programs.

Validating [sumas](https://omegaup.com/arena/problem/sumas), You can use the following code in C++17:

```cpp
#include <iostream>
#include <fstream>

int main() {
  // Reads "data.in" to get the original input.
  int64_t a, b;
  {
    std::ifstream input("data.in", std::ifstream::in);
    input >> a >> b;
  }
```



