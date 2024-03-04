# Password Generator
The purpose of this task is to create a password based on the user's desired requirements and also allow two password difficulties.

### Skills
- Use Python user input to track how many of each password character the user desires.
- The easy difficulty will just give a password with the order of the characters not randomized.
    - Use for loops along with redundant variables to randomize the character chosen for each type and concatenate it to the password.
    - Use the random module to randomize your choice from the lists that contain the characters.
- The hard difficulty will randomize the order of the characters, increasing the difficulty of cracking the password.
    - Create a list to store all of the characters of the password.
    - Using the rnadom module, use the shuffle method to shuffle the characters and then use a 4th for loop to add all the characters into the password `str`.
- If neither hard or easy is entered, check the exception.
