# TrustQR – Technical Architecture

## 1. Project Overview
TrustQR is a cybersecurity prototype designed to help users identify potentially suspicious QR-code links before opening them.

## 2. System Workflow
1. User provides a QR-code image or decoded URL.
2. The application extracts or receives the URL.
3. The system checks the URL for suspicious patterns.
4. The application displays a warning or review result.
5. The user decides whether to proceed.

## 3. Architecture Components
- Input: QR-code image or URL
- Processing: Python application
- Validation: Basic URL and suspicious-pattern checks
- Output: Safety result and warning message

## 4. Technologies
Python, HTML, CSS, and JavaScript (where implemented).

## 5. Limitations
This prototype cannot guarantee that a URL is safe. Users should verify payment details independently and avoid entering sensitive information on suspicious websites.
