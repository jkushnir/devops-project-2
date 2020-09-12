# devops-project-2

My second project for the Devops Experts course.
The project is a set of three text-based games, with the scoreboard running as a web server (reading the score from a text file).
Project contains a test script, which, using a selenium webdriver, connects to the scores server and confirms that the score is between 0 and 1000.

Everything except the test is running in a docker container, with the test running via a Jenkins (Jenkinsfile created with Blue Ocean)
