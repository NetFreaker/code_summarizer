# 🧠 Code Summarizer using CodeT5

A Streamlit-based web application that generates natural language summaries for code snippets using the fine-tuned **Salesforce/CodeT5** model. Built as part of a course project for **CIS 581: Advanced Software Engineering** at **California State University, Dominguez Hills**.

## 👨‍🎓 Author

**Rahul Kavati**
Course: CIS 581 – Advanced Software Engineering
Instructor: Dr. Alireza Izaddoost
University: CSUDH

---

## 🚀 Features

* Accepts source code in Python, Java, JavaScript, and other supported languages
* Uses `Salesforce/codet5-base-multi-sum` to generate summaries
* Clean two-column UI using Streamlit
* Useful for code documentation, onboarding, or reverse engineering

---

## 🚫 Requirements

* Python 3.8+
* Recommended to use a virtual environment

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔄 Run the App

```bash
streamlit run app.py
```

If you encounter `torch._C._get_custom_class_python_wrapper` or file watcher errors:

```bash
streamlit run app.py --server.runOnSave=false
```

---

## 📚 Example Test Inputs

### Example 1

```python
def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count
```

**Expected Summary:**

> Calculates the average of a list of numbers.

### Example 2

```java
public boolean isEven(int num) {
    return num % 2 == 0;
}
```

**Expected Summary:**

> Checks if a number is even.

### Example 3

```python
def is_palindrome(s):
    return s == s[::-1]
```

**Expected Summary:**

> Determines if a string is a palindrome.

---

## 🚜 Model Info

* **Model**: `Salesforce/codet5-base-multi-sum`
* **Architecture**: Seq2Seq transformer
* **Trained on**: Multiple programming languages and summarization benchmarks

More info: [https://huggingface.co/Salesforce/codet5-base-multi-sum](https://huggingface.co/Salesforce/codet5-base-multi-sum)

---

## 📄 File Structure

```
code_summarizer/
├── app.py            # Streamlit UI
├── summarizer.py     # Model logic
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 🚀 Future Improvements

* Add support for LLMs like CodeLLaMA or StarCoder
* Include side-by-side code explanation and visualization
* Add file upload support

---