## Project Title :- DIGITAL RESUME CHECKER
Name :- AASHVI NAGORI
Registration No. - 25BSA10133

## Overview of the project :
The Digital Resume Checker is a program designed to check and analyze resumes effectively using keywords matching and scoring data. This project helps students, job applicants, and companies by providing a quick and friendly way of resume based on important skill such as technical skills, communication skills, experiences and past-behaviour . 

## Features :
1. Automated Resume checking  :-
 This system  reads and processes resume content from a text file, which helps to eliminate the need of review and saves time.
2. Keyword-Based Skill Matching :-
 It compares the resume content with technical and non-technical skill keywords by arrays and sorting for accurate detection of relevant skills.
3. Use of NumPy library :-
 NumPy is used to manage keyword arrays, proper matches for the job and deals with scoring result accurately.
4. Matplotlib (Graphical Result Visualization)  :-
 The bar chart is created using Matplotlib to visually show performance in categories like technical skills, soft skills, and resume structure.

## Technologies and Tools used :-
1.python programming language.
2.numpy library
3.matplot library
4.arrays and sorting
<br>

## Steps to install and run the project :-
1. Install Python :-
 The phython version 3.8 or any can be used on your system.
2. Install Required Python Libraries
The project requires two phython modules like numpy and matplotlib.
3. Prepare Resume File :
  The resume must be saved in .txt format.
4. Run the Program :
Open a terminal or command , navigate to the project folder:
cd Desktop / Digital Resume Checker 
5. Run the script using:
  Python resume_checker.py
6. Enter Input 
The system will ask:
Enter the resume file name for example resume.txt 
7. View Results :
After starting the program will display:
Matching technical and non-technical skills result
Missing resume 
Final average resume score

A bar graph will automatically open showing Category Performance.
<br>

## Instruction for testing :-
1. Test with Multiple Resume Files
Prepare different .txt resumes to test the system’s result :
Resume Type	Expected Result
Complete Resume	High score with fewer suggestions
Resume Missing Skills	Lower skill score + proper feedback
Multiple missing report alerts    Resume with Many Keywords	
High keyword match result
Empty or Very Short File	Very low score + missing warningsss

2. Required Keyword Matching
Check whether:
Technical skills are correctly identified .
Non-technical and  terms are recognized.
Resume sections are marked present only if they exist in the text.

3. Confirm Scoring Calculation
Verify the scoring pattern :
Technical skill matches affect the  score.
Non-technical match also affects the score.
Missing resume sections reduce the total score.
Run multiple resumes and ensure the score changes accordingly .

4. Test File Output
After each result, 

check resume analysis output.txt
it may contain Resume Score
Improvement Suggestions


5. Test Graph Generation
Confirm that:
A bar graph is displayed showing category scores.
Values match those shown in the page .
Application does not crash when values are zero.

6. Repeatability Test
Run the same resume multiple times and ensure:
Output score remains constant.
Graph and text output match previous results .

7.Document Results
Record observations including:
Errors identified
Scores obtained
System responses
Suggestions generated
