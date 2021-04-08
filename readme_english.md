# game like "Million Dollar Money Drop"
A game similar to "Million Dollar Money Drop". Database of questions under development. For now only backend, frontend version of pygame in preparation.

# Preparation:
The idea for the game was born as the first python project.
In the initial phase, the game was supposed to be a simple game - in fact, it still remains - where points are scored for each correct answer, while developing the code, new ideas and functionalities appeared.

# Program development process and difficulties encountered along the way:
1. I started by writing a code that added a point for each correct answer. Only one answer could be chosen for each question, and the questions themselves were asked in sequence.
2. For testing purposes I created a json file with a set of questions. Each question was assigned four answer suggestions and a correct answer.
3. Then I added a functionality in which the questions are randomized, which made each game could be different, and the option of ending the game after answering incorrectly
4. The idea of transforming the game into those of the 'Million Dollar Money Drop' type appears - therefore I added the category of each question to the json file, and in the program code I set an option in which two categories are drawn first and the player chooses one of them, then it falls a question appropriate for the selected category. The problem at this stage was that the same category was drawn twice. The player still could only choose one answer.
5. To get closer to the original I introduced the option of placing any amount on each of the proposed answers. Then I wrote a code that verified if there was any amount other than zero under the correct answer and assigned the amount from this answer as the amount won in the game. The problem at this stage turned out to be overwriting the correct answer, therefore the program always saw two answers as correct, overwriting the winning amount with no limit, no end of the game with a zero amount
6. At this stage, the priority was to check the rates correctly with the correct answer, if the answer was correct, then adding the rate to the winning amount, fixing the winning limit error
7. Setting the maximum number of questions, setting the question level depending on the stage of the game: displaying four answers for questions 1-4, displaying three answers for questions 5-7, displaying two possible answers in the final 8 question, adding the question level in the json file
8. Option informing about the end of the game when the amount drops to PLN 0
9. Shortening the code by define a function category(question, random_index) which turned out to be defective, a bug appeared that matched the category 1 of the answers from category 2 and vice versa, the bug was fixed, but the functionality of this definition turned out to be insufficient
10. !!! the biggest problem in the program !!! which I have not fully resolved, is the problem with selecting the appropriate level of the question, there was a large bug that caused the program to display a four-answer question (from level 1-4) when it should randomize three or two-answer questions (level 5-8). Due to the lack of display of C and D responses that were in the json source file, the program closed with an error.
11. Because I couldn't solve the problem with indexing the questions by level, I decided to create three instead of one json file, one for each of the question levels
12. I created a function that randomizes the question depending on the level
13. Created a list of used questions and conditioning of the level of the game depending on its length
14. Two-category printing function and the ability to choose one of them
15. Function of printing questions and answers after selecting the category
16. Bidding function for specific answers, no limit and all answers can be bet
17. Checking the answer, checking what stakes were placed and writing down the won temporary amount
18. Setting stake limits, automatic calculation of the winnings after writing the answer, limit of the winning amount
19. Function forcing one blank answer
20. Function forcing the stake to jump to 25,000, consisting in rounding the amount given by the player to the nearest, divisible by 25
21. Shorten the codes by half through definitions and the appropriate setting of the loop and \n print
22. Creating a separate function that checks the correct answer
23. The creation of the flow of the game function

The key element for the next stage of the game is to add the question-avoidance function and work on the frontend version of the game

All comments and tips on how to improve the code are welcome :) 
