# 📝 Simple Tkinter Text Editor
This is a simple text editor built using the Tkinter library in Python. It features basic functionalities like creating a new document, opening and saving text files, text manipulation, and word count. 🚀
<br />

✨ Features: 

  * New Document 🆕: Start a new document, with an option to discard unsaved changes.
  
  * Save Document 💾: Save the text written to a file with a .txt extension.
  
  * Open Document 📂: Open an existing text file and display its contents.
  
  * Copy 📋: Copy selected text to the clipboard.
  
  * Paste ⬇️: Paste clipboard content at the cursor's position.
  
  * Clear ❌: Clear all text from the editor.
  
  * Word Count 📊: Displays the total number of words in the current text.
<br />

🧑‍💻 Code Overview 
Class Application: This class extends the Frame widget from Tkinter and contains the primary logic for the text editor.

Widgets:

 * A Text widget for the main text input area.

 * A menu bar with options for File, Edit, and Tools functionalities.

Functions:

 * newDoc(): Prompts the user to start a new document and discard any unsaved changes.

 * saveDoc(): Saves the current content to a file chosen by the user.

 * openDoc(): Opens an existing text file and displays its content in the editor.

 * copy(): Copies the selected text to the clipboard.

 * paste(): Pastes the clipboard content at the current cursor position.

 * clear(): Clears all text in the editor.

 * wordCount(): Counts the number of words in the current text and shows the count in a pop-up message.
