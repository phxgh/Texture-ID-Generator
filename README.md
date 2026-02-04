# Texture ID Generator
This is a simple script that I use to generate my texture IDs within my odin projects. Generally, I add this into my build/run scripts whenever I'm editing a project, usually with the line<br>
`py gen_tex_id.py` on Windows, and<br>
`python3 gen_tex_id.py` on macOS/Linux.<br>
These should come before you build your actual project that way the IDs are generated properly!

## Usage
You can add this to your tools/scripts folder within your project directory. You may change the path of the textures, directory/name of the generated file, the package name, and the name of the generated enum with the respective constants at the top of the file.<br>
Then, just run the script before you build your project. As long as the IDs exist in the same package as the rest of your code, you'll be able to use the IDs all across your project!
