import gradio as gr

def display_answer(answer):
    return answer

with gr.Blocks() as demo:
    gr.Markdown("# 1000 Flashcards ( General, Sports, Technical,Space ) ")
    gr.Markdown("---")

    with gr.Row():
        gr.Markdown("**What is the capital of France?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Paris."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The human heart has three chambers.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, the human heart has four chambers."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest ocean on Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Pacific Ocean."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who painted the Mona Lisa?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Leonardo da Vinci."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Japan?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tokyo."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Great Wall of China is visible from space.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, it's a myth that the Great Wall of China is visible from space."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for gold?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Au."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote '1984'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("George Orwell."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the smallest planet in our Solar System?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mercury."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Bananas grow on trees.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, bananas grow on large herbaceous plants."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Canada?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ottawa."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who discovered penicillin?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Fleming."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the tallest mountain in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mount Everest."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Dolphins are fish.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, dolphins are mammals."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest desert in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sahara Desert."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'To Kill a Mockingbird'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Harper Lee."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the hardest natural substance on Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Diamond."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Humans have more than 5 senses.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, humans have more than 5 senses."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest planet in our Solar System?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jupiter."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'The Odyssey'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Homer."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for water?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("H2O."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Sun is a star.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, the Sun is a star."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Italy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Rome."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who painted 'The Starry Night'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Vincent van Gogh."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the most abundant gas in the Earth's atmosphere?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Nitrogen."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Amazon is the longest river in the world.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, the Nile is the longest river in the world."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Russia?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Moscow."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the telephone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Graham Bell."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest mammal in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The blue whale."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Light travels faster than sound.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, light travels faster than sound."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Germany?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Berlin."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'Pride and Prejudice'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jane Austen."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the currency of the United Kingdom?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pound Sterling."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: An octopus has three hearts.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, an octopus has three hearts."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of India?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("New Delhi."), outputs=txt)


    with gr.Row():
        gr.Markdown("**What is the capital of Australia?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Canberra."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Atlantic Ocean is the largest ocean on Earth.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, the Pacific Ocean is the largest."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the author of 'Harry Potter'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("J.K. Rowling."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for iron?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Fe."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The human body has four lungs.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, the human body has two lungs."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Brazil?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Brasilia."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who painted 'The Last Supper'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Leonardo da Vinci."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the speed of light?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 299,792 kilometers per second (186,282 miles per second)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Great Wall of China is the only man-made structure visible from space.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, there are other man-made structures visible from space."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Egypt?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cairo."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the author of 'Pride and Prejudice'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jane Austen."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest continent on Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Asia."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Humans share 50% of their DNA with bananas.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, humans share approximately 50% of their DNA with bananas."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Argentina?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Buenos Aires."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the author of 'The Great Gatsby'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("F. Scott Fitzgerald."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the smallest bone in the human body?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The stapes (or stirrup) bone in the middle ear."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Eiffel Tower is taller than the Statue of Liberty.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, the Eiffel Tower is taller than the Statue of Liberty."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Spain?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Madrid."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who developed the theory of relativity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Albert Einstein."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the longest river in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Nile River."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Great Pyramid of Giza is one of the Seven Wonders of the Ancient World.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, the Great Pyramid of Giza is one of the Seven Wonders of the Ancient World."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Mexico?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mexico City."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'Romeo and Juliet'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("William Shakespeare."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the hardest natural substance?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Diamond."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The capital of Australia is Sydney.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, the capital of Australia is Canberra."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of China?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Beijing."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who discovered gravity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sir Isaac Newton."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest organ in the human body?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The skin."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Sharks are mammals.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, sharks are fish."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of South Africa?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pretoria (administrative), Bloemfontein (judicial), and Cape Town (legislative)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'The Catcher in the Rye'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("J.D. Salinger."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the most spoken language in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mandarin Chinese."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The human skeleton is made up of over 300 bones.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, an adult human skeleton has 206 bones."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Greece?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Athens."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Greece?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Athens."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who painted 'The Scream'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Edvard Munch."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest planet in our solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jupiter."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: A leap year has 365 days.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, a leap year has 366 days."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Canada?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ottawa."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who developed the theory of general relativity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Albert Einstein."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the smallest country in the world by area?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Vatican City."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Humans have 46 chromosomes.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, humans have 46 chromosomes."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Italy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Rome."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who painted 'The Persistence of Memory'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Salvador Dalí."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the longest river in Africa?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Nile River."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Earth is the fourth planet from the Sun.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, the Earth is the third planet from the Sun."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Japan?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tokyo."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'Moby-Dick'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Herman Melville."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest island in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Greenland."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Venus is the hottest planet in our solar system.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, Venus is the hottest planet in our solar system."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Russia?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Moscow."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who developed the laws of motion?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Isaac Newton."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the longest bone in the human body?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The femur."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Great Wall of China is more than 10,000 kilometers long.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, the Great Wall of China is more than 10,000 kilometers long."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of the United States?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Washington, D.C."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'The Adventures of Huckleberry Finn'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mark Twain."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest ocean on Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Pacific Ocean."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Mars is known as the Red Planet.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, Mars is known as the Red Planet."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of India?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("New Delhi."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who painted the ceiling of the Sistine Chapel?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Michelangelo."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for gold?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Au."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The Sahara is the largest desert in the world.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, the Sahara is the largest hot desert in the world."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Australia?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Canberra."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'The Odyssey'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Homer."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the smallest planet in our solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mercury."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: There are 50 states in the USA.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, there are 50 states in the USA."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the capital of Brazil?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Brasilia."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who wrote 'Don Quixote'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Miguel de Cervantes."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest animal on Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The blue whale."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does HTTP stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("HyperText Transfer Protocol."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the time complexity of binary search?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("O(log n)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Python is a statically typed language.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, Python is a dynamically typed language."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does SQL stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Structured Query Language."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is known as the father of computer science?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alan Turing."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of the 'git clone' command?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To create a copy of an existing Git repository."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: An IP address uniquely identifies a device on a network.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, an IP address uniquely identifies a device on a network."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does CSS stand for in web development?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cascading Style Sheets."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the time complexity of bubble sort?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("O(n^2)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the function of DNS in networking?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To translate domain names to IP addresses."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: JSON stands for JavaScript Oriented Notation.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False, JSON stands for JavaScript Object Notation."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the main purpose of a firewall in network security?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To monitor and control incoming and outgoing network traffic based on security rules."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does RAM stand for in computing?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Random Access Memory."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: TCP/IP is a protocol suite used for communication over the internet.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, TCP/IP is a protocol suite used for communication over the internet."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the primary function of an operating system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To manage the computer's hardware and software resources and provide common services for computer programs."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does GPU stand for in computer hardware?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Graphics Processing Unit."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: The OSI model has 7 layers.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, the OSI model has 7 layers."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the command to list all files and directories in Linux?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("ls"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the full form of HTML?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("HyperText Markup Language."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: IPv6 uses 128-bit addresses.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, IPv6 uses 128-bit addresses."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the difference between '=='' and '===' in JavaScript?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("'==' checks for equality of value, while '===' checks for equality of value and type."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does 'API' stand for in software development?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Application Programming Interface."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: A linked list is a linear data structure.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, a linked list is a linear data structure."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the primary use of a database index?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To improve the speed of data retrieval operations."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does 'JSON' stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("JavaScript Object Notation."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: REST stands for Representational State Transfer.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, REST stands for Representational State Transfer."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of the 'mv' command in Linux?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To move or rename files and directories."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does DNS stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Domain Name System."), outputs=txt)

    with gr.Row():
        gr.Markdown("**True or False: Docker is a tool used for virtualization.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True, Docker is a tool used for containerization, which is a form of virtualization."), outputs=txt)
        
#neww
    

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 5\ny = 2\nprint(x / y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("2.5"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 3\nprint(x // y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("3"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of `a` after executing the following code snippet?**\n\n```python\na = 5\na += 3\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("8"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = True\ny = False\nprint(x and y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = True\ny = False\nprint(x or y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = True\nprint(not x)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 5\nprint(x == y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 10\nprint(x != y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 5\nprint(x > y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 5\nprint(x < y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("False"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 10\nprint(x >= y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 5\ny = 5\nprint(x <= y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("True"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 2\ny = 5\nif x > y:\n    print('x is greater than y')\nelse:\n    print('y is greater than x')\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("y is greater than x"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 5\ny = 5\nif x == y:\n    print('x is equal to y')\nelse:\n    print('x is not equal to y')\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("x is equal to y"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 7\ny = 10\nif x > y:\n    print('x is greater than y')\nelif x < y:\n    print('x is less than y')\nelse:\n    print('x is equal to y')\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("x is less than y"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n\n```python\nx = 10\ny = 10\nif x != y:\n    print('x is not equal to y')\nelse:\n    print('x is equal to y')\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("x is equal to y"), outputs=txt)



#newscience


    with gr.Row():
        gr.Markdown("**What is the chemical symbol for water?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("H2O"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for oxygen?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("O"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for carbon?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("C"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for sodium?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Na"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for potassium?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("K"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for gold?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Au"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for silver?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ag"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for iron?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Fe"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for copper?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cu"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for helium?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("He"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for nitrogen?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("N"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for phosphorus?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("P"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for sulfur?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("S"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for calcium?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ca"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for magnesium?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mg"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for mercury?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hg"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for lead?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pb"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for uranium?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("U"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for tin?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sn"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for silicon?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Si"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for carbon dioxide?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("CO2"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for methane?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("CH4"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for ammonia?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("NH3"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for hydrochloric acid?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("HCl"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for sulfuric acid?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("H2SO4"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for nitric acid?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("HNO3"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for hydrofluoric acid?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("HF"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for sodium hydroxide?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("NaOH"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the chemical symbol for potassium hydroxide?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("KOH"), outputs=txt)

#newplanet
    
    with gr.Row():
        gr.Markdown("**Which planet is closest to the Sun?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mercury"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is the largest in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jupiter"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known as the 'Red Planet'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mars"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet has the most moons in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jupiter"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known as the 'Evening Star' or 'Morning Star'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Venus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the smallest planet in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mercury"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the hottest planet in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Venus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known as the 'Blue Planet' due to its color?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Earth"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet has the most prominent rings?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Saturn"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is sometimes called Earth's 'sister planet'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Venus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet has the longest day in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Venus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is famous for its Great Red Spot?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jupiter"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known as the 'Ice Giant'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Uranus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is often referred to as the 'God of the Sea'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Neptune"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known for its distinct, bright rings?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Saturn"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet has the shortest year in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mercury"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is famous for its extreme axial tilt?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Uranus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known for its beautiful, icy rings?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Saturn"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is often called the 'Ice Dwarf'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pluto"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is closest in size to Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Venus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which planet is known as the 'Gas Giant'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jupiter"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the most abundant gas in the atmosphere of Mars?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Carbon Dioxide"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest moon in the solar system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ganymede"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which moon is known for its icy geysers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Enceladus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which moon is the only moon in the solar system with a dense atmosphere?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Titan"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the largest moon of Mars?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Phobos"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which moon is known for its many volcanic features?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Io"), outputs=txt)

    
    
#new
    with gr.Row():
        gr.Markdown("**What is the name of our galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Milky Way"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a group of stars, gas, dust, and dark matter bound together by gravity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Galaxy"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nearest galaxy to the Milky Way?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the small, dense remnant of a star that has collapsed under gravity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Black hole"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a massive, luminous sphere of plasma held together by gravity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Star"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the most abundant element in the universe?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hydrogen"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for the explosive death of a massive star?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Supernova"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name given to the remnants of a supernova explosion?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Neutron star"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a cloud of gas and dust in space where stars are born?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Nebula"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a small, dense remnant of a star that has exhausted its nuclear fuel?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("White dwarf"), outputs=txt)


#newseq


    with gr.Row():
        gr.Markdown("**What is Artificial Intelligence (AI)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("AI is the simulation of human intelligence processes by machines, especially computer systems."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What are the two main types of AI?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The two main types of AI are Narrow AI (Weak AI) and General AI (Strong AI)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Give an example of Narrow AI (Weak AI).**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Virtual personal assistants like Siri, Cortana, and Alexa are examples of Narrow AI."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Machine Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Machine Learning is a subset of AI that provides systems the ability to automatically learn and improve from experience without being explicitly programmed."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Deep Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Deep Learning is a subset of Machine Learning where artificial neural networks, algorithms inspired by the human brain, learn from large amounts of data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Natural Language Processing (NLP)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Natural Language Processing is a branch of AI that enables computers to understand, interpret, and generate human language."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Computer Vision?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Computer Vision is a field of AI that enables computers to interpret and understand the visual world through digital images, videos, and deep learning models."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Turing Test?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Turing Test is a test of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Reinforcement Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Reinforcement Learning is a type of Machine Learning where an agent learns to make decisions by trial and error, receiving feedback from its environment."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What are some applications of AI in everyday life?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Some applications of AI in everyday life include virtual personal assistants, recommendation systems, image and speech recognition, and autonomous vehicles."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Overfitting in Machine Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Overfitting occurs when a model learns the detail and noise in the training data to the extent that it negatively impacts the performance of the model on new data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the difference between Supervised Learning and Unsupervised Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("In Supervised Learning, the model is trained on labeled data, while in Unsupervised Learning, the model is trained on unlabeled data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the role of Artificial Neural Networks (ANNs) in Deep Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Artificial Neural Networks are the building blocks of Deep Learning, functioning similar to the human brain's neural network to process complex patterns and inputs."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Transfer Learning in Machine Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Transfer Learning is a Machine Learning technique where a model trained on one task is reused as the starting point for a model on a second task."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What are some ethical considerations in AI development and deployment?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ethical considerations in AI include bias and fairness, transparency and explainability, accountability, data privacy, and the impact on jobs and society."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the goal of AI safety research?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The goal of AI safety research is to ensure that AI systems are safe, reliable, and aligned with human values, minimizing the risks associated with AI development and deployment."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is GAN (Generative Adversarial Network)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("GAN is a class of machine learning systems where two neural networks contest with each other in a game, with one generating new data instances and the other evaluating them."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is AI Explainability?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("AI Explainability refers to the ability to explain the decision-making process and outcomes of AI systems in a way that is understandable to humans."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the role of Data Preprocessing in Machine Learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Data Preprocessing involves transforming raw data into a format suitable for Machine Learning models, including cleaning, normalization, and feature engineering."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Bias in AI?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Bias in AI refers to systematic errors or inaccuracies in AI systems that result in unfair outcomes, often due to incomplete or unrepresentative training data."), outputs=txt)

   
#neqq


    with gr.Row():
        gr.Markdown("**Who is known as the 'God of Cricket'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sachin Tendulkar"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the highest individual score by a batsman in Test cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("400* by Brian Lara"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a hat-trick in cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("When a bowler takes three wickets in consecutive deliveries in the same match."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country won the first Cricket World Cup?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("West Indies"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who holds the record for the fastest century in One Day Internationals (ODIs)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("AB de Villiers (South Africa)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the trophy awarded to the winner of the Ashes series between England and Australia?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Ashes Urn"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the only cricketer to score a triple century in Test, double century in ODI, and century in T20I cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Chris Gayle (West Indies)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nickname of the Australian cricket team?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Baggy Greens"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which player has taken the most wickets in Test cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Muttiah Muralitharan (Sri Lanka)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the longest format of cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Test cricket"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country has won the most Cricket World Cups?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Australia"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is known as the 'Sultan of Swing'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Wasim Akram (Pakistan)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the highest run-scorer in One Day Internationals (ODIs)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sachin Tendulkar (India)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the trophy awarded to the winner of the ICC Champions Trophy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The ICC Champions Trophy"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is known as 'The Wall' in Indian cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Rahul Dravid"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which cricket stadium is known as the 'Home of Cricket'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Lord's Cricket Ground (England)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a situation in cricket where a team wins without losing any wickets in the entire match?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Winning by ten wickets"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the fastest bowler in the history of cricket in terms of recorded speed?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Shoaib Akhtar (Pakistan)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the highest team total in a Test innings?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("952/6 declared by Sri Lanka against India in 1997"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who has hit the most sixes in international cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Shahid Afridi (Pakistan)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who was the first cricketer to score a double century in One Day Internationals (ODIs)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sachin Tendulkar (India)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the trophy awarded to the winner of the Indian Premier League (IPL)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The IPL Trophy"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the fastest player to reach 10,000 runs in One Day Internationals (ODIs)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Virat Kohli (India)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who has taken the most catches in Test cricket?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Rahul Dravid "),outputs=txt)

#nnnn

    with gr.Row():
        gr.Markdown("**Who won the FIFA World Cup in 2018?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("France"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which player has won the most Ballon d'Or awards?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Lionel Messi"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the football stadium known as 'Theatre of Dreams'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Old Trafford"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country has won the most FIFA World Cup titles?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Brazil"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the all-time leading goalscorer in the UEFA Champions League?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cristiano Ronaldo"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which club has won the most UEFA Champions League titles?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Real Madrid"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the current manager of Liverpool FC?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jurgen Klopp"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which player has scored the most goals in a single Premier League season?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mohamed Salah"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nickname of the Argentine national football team?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("La Albiceleste"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the only player to have won the UEFA Champions League with three different clubs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Clarence Seedorf"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the football stadium known as 'The Kop'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Anfield"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country won the first FIFA World Cup?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Uruguay"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who has won the most Premier League titles as a manager?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sir Alex Ferguson"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which club has won the most FA Cup titles?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Arsenal"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the all-time leading scorer for the Spanish national team?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("David Villa"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nickname of the Italian national football team?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Gli Azzurri"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who won the UEFA European Championship in 2016?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Portugal"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nickname of the Manchester United Football Club?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Red Devils"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the all-time leading scorer for the German national team?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Miroslav Klose"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which player has won the most FIFA Ballon d'Or awards?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Lionel Messi"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the current manager of Manchester City FC?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pep Guardiola"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country won the UEFA European Championship in 2008?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Spain"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nickname of the Brazilian national football team?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Seleção"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the all-time leading scorer for the English Premier League?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alan Shearer"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which player has won the most UEFA European Championship titles?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cristiano Ronaldo"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who won the Copa America in 2019?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Brazil"), outputs=txt)


##tts

    with gr.Row():
        gr.Markdown("**Which city hosted the first modern Olympic Games in 1896?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Athens, Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What do the Olympic rings represent?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The five continents of the world: Africa, the Americas, Asia, Europe, and Oceania"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which athlete has won the most gold medals in Olympic history?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Michael Phelps (United States)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**In which year did women first compete in the Olympic Games?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("1900"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Olympic motto?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Citius, Altius, Fortius (Faster, Higher, Stronger)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country has won the most Olympic gold medals overall?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("United States"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who was the first athlete to light the Olympic flame at the opening ceremony?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Spyridon Louis (Greece)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the highest award given to Olympic athletes?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Olympic Gold Medal"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which city has hosted the most Olympic Games?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("London (United Kingdom)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the Olympic mascot for the 2020 Tokyo Olympics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Miraitowa"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country boycotted the 1980 Summer Olympics held in Moscow?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("United States"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the athlete who famously raised his fist in a Black Power salute at the 1968 Olympics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tommie Smith"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the minimum age requirement for athletes to compete in the Olympic Games?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("There is no minimum age requirement"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which city will host the 2024 Summer Olympics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Paris, France"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the traditional Olympic sport in which competitors slide a stone on a sheet of ice towards a target area?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Curling"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the athlete known as 'The Flying Finn' and won nine Olympic gold medals in long-distance running?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Paavo Nurmi (Finland)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which city hosted the 2016 Summer Olympics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Rio de Janeiro, Brazil"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the symbol representing the Olympic Games?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Olympic flame"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country won the first Olympic basketball gold medal in 1936?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("United States"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the highest award given to Olympic athletes?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Olympic Gold Medal"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the only athlete to have won Olympic gold medals in both the Winter and Summer Olympics in different sports?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Eddie Eagan (United States)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which country has won the most gold medals in a single Summer Olympics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("United States (1984 Summer Olympics)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the Olympic medal for third place?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Bronze Medal"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the venue that hosts the opening and closing ceremonies of the Olympic Games?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Olympic Stadium"), outputs=txt)


##tns

    with gr.Row():
        gr.Markdown("**What is the stock market?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The stock market is a place where stocks (shares of ownership in a company) are bought and sold."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a stock exchange?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A stock exchange is a marketplace where securities like stocks, bonds, and commodities are bought and sold."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a stock?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A stock represents ownership in a company and entitles the owner to a share of the company's assets and profits."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the difference between a stock and a bond?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Stock represents ownership in a company, while a bond represents a loan made to a corporation or government in exchange for regular interest payments."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a bull market?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A bull market is a financial market condition where prices of securities are rising or expected to rise."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a bear market?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A bear market is a financial market condition where prices of securities are falling or expected to fall."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the role of a stockbroker?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A stockbroker acts as an intermediary between buyers and sellers of stocks and other securities."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a dividend?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A dividend is a payment made by a corporation to its shareholders, usually in the form of cash or additional shares."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is insider trading?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Insider trading is the buying or selling of a security by someone who has access to material, non-public information about the security."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a stock split?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A stock split is a corporate action where a company divides its existing shares into multiple shares to boost the liquidity of the shares."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a blue-chip stock?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A blue-chip stock is the stock of a large, well-established, and financially sound company with a history of reliable performance and stable earnings."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a stop-loss order?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A stop-loss order is an order placed with a broker to buy or sell a security once the security reaches a certain price, known as the stop price."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is day trading?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Day trading is a trading strategy where traders buy and sell financial instruments within the same trading day, with all positions closed before the market closes."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a mutual fund?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A mutual fund is a professionally managed investment fund that pools money from many investors to invest in stocks, bonds, or other securities."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a futures contract?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A futures contract is a legally binding agreement to buy or sell a commodity or financial instrument at a predetermined price at a specified time in the future."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a margin call?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A margin call is a broker's demand for additional funds or securities to cover a shortfall in the margin account."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Dow Jones Industrial Average (DJIA)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Dow Jones Industrial Average is a stock market index that measures the stock performance of 30 large, publicly-owned companies listed on stock exchanges in the United States."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a penny stock?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A penny stock is a common stock that typically trades for less than $5 per share and is considered highly speculative and risky."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a market order?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A market order is an order to buy or sell a security at the best available price in the current market."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a limit order?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A limit order is an order to buy or sell a security at a specific price or better."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Nasdaq Composite Index?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Nasdaq Composite Index is a stock market index that includes all stocks listed on the Nasdaq stock market, representing primarily technology and internet-related companies."), outputs=txt)

##rrr

    with gr.Row():
        gr.Markdown("**Who invented the telephone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Graham Bell"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is credited with inventing the light bulb?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Thomas Edison"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tim Berners-Lee"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is known for inventing the phonograph?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Thomas Edison"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical airplane?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Wright Brothers"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the printing press?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Johannes Gutenberg"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first successful polio vaccine?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Jonas Salk"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is credited with inventing the radio?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Guglielmo Marconi"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the steam engine?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("James Watt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical automobile?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Karl Benz"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is credited with inventing the first mechanical computer?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Charles Babbage"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the microwave oven?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Percy Spencer"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the dynamite?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alfred Nobel"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the sewing machine?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Elias Howe"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the electric battery?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alessandro Volta"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the air conditioner?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Willis Carrier"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is credited with inventing the first practical telephone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Graham Bell"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical electric light bulb?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Thomas Edison"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the theory of relativity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Albert Einstein"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tim Berners-Lee"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is known for inventing the phonograph and the motion picture camera?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Thomas Edison"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first successful airplane?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Wright Brothers"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the ballpoint pen?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("László Bíró"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tim Berners-Lee"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical telephone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Graham Bell"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the theory of general relativity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Albert Einstein"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical airplane?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Wright Brothers"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the steam engine?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("James Watt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tim Berners-Lee"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical telephone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Graham Bell"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tim Berners-Lee"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first successful airplane?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Wright Brothers"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the electric battery?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alessandro Volta"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the steam engine?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("James Watt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the first practical automobile?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Karl Benz"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the telephone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Alexander Graham Bell"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the light bulb?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Thomas Edison"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who invented the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tim Berners-Lee"), outputs=txt)

#eee

    with gr.Row():
        gr.Markdown("**What is the speed of light in a vacuum?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 299,792 kilometers per second (km/s)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who formulated the theory of general relativity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Albert Einstein"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Newton's First Law of Motion?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("An object at rest stays at rest, and an object in motion stays in motion, unless acted upon by an external force."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of force in the International System of Units (SI)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Newton (N)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for kinetic energy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Kinetic Energy = 1/2 * mass * velocity^2 (KE = 1/2 mv^2)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who discovered the law of universal gravitation?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Isaac Newton"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of the acceleration due to gravity on Earth's surface?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 9.8 meters per second squared (m/s^2)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the principle of superposition?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The principle that states that the total displacement caused by two or more waves is the sum of the individual displacements caused by each wave."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Ohm's Law?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ohm's Law states that the current through a conductor between two points is directly proportional to the voltage across the two points. (V = IR)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of electric charge?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Coulomb (C)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the principle of conservation of energy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Energy cannot be created or destroyed, only transformed from one form to another."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who developed the laws of motion and universal gravitation?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Isaac Newton"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for calculating work done?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Work Done = Force * Distance (W = Fd)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of power in the International System of Units (SI)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Watt (W)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the definition of momentum?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Momentum is the product of the mass and velocity of an object. (p = mv)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of frequency?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hertz (Hz)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Doppler effect?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Doppler effect is the change in frequency or wavelength of a wave in relation to an observer moving relative to the wave source."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the speed of sound in air at room temperature?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 343 meters per second (m/s)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who proposed the quantum theory?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Max Planck"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of magnetic flux?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Weber (Wb)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the principle of uncertainty?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Heisenberg's Uncertainty Principle states that it is impossible to simultaneously measure the exact position and momentum of a particle."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of capacitance?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Farad (F)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for potential energy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Potential Energy = mass * gravity * height (PE = mgh)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the second law of thermodynamics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The second law of thermodynamics states that the total entropy of an isolated system always increases over time."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Hooke's Law?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hooke's Law states that the force needed to extend or compress a spring is directly proportional to the distance it is stretched or compressed. (F = kx)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of inductance?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Henry (H)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Coulomb's Law?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Coulomb's Law states that the force between two charged objects is directly proportional to the product of the charges and inversely proportional to the square of the distance between them."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who discovered the electron?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("J.J. Thomson"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the unit of pressure?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pascal (Pa)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for calculating density?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Density = mass/volume (ρ = m/V)"), outputs=txt)

#eeeerrrrr

    with gr.Row():
        gr.Markdown("**What is the value of pi (π) to two decimal places?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("3.14"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Pythagorean theorem?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("In a right-angled triangle: a^2 + b^2 = c^2"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of the square root of 144?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("12"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the derivative of x^2?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("2x"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the area of a circle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Area = πr^2"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of e (Euler's number) to two decimal places?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("2.72"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the quadratic formula?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("x = (-b ± √(b^2 - 4ac)) / 2a"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the integral of 1/x dx?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("ln|x| + C"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the sum of the angles in a triangle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("180 degrees"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of sin(90°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("1"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the circumference of a circle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Circumference = 2πr"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of cos(0°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("1"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the volume of a sphere?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Volume = 4/3πr^3"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of tan(45°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("1"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the area of a triangle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Area = 1/2 * base * height"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the binomial theorem?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("(a + b)^n = Σ (n choose k) a^(n-k) b^k"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of log(1)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("0"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of the golden ratio?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 1.618"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the slope of a line?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Slope = (y2 - y1) / (x2 - x1)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the area of a rectangle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Area = length * width"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the volume of a cylinder?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Volume = πr^2h"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for calculating compound interest?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A = P(1 + r/n)^(nt)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the area of a parallelogram?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Area = base * height"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the perimeter of a rectangle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Perimeter = 2(length + width)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of cos(90°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("0"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the sum of the interior angles of a pentagon?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("540 degrees"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of sin(0°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("0"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the area of a trapezoid?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Area = 1/2 * (base1 + base2) * height"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the volume of a cone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Volume = 1/3πr^2h"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of tan(0°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("0"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the surface area of a sphere?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Surface Area = 4πr^2"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the value of sin(30°)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("1/2"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the formula for the volume of a rectangular prism?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Volume = length * width * height"), outputs=txt)


#TYYYY


    with gr.Row():
        gr.Markdown("**What is the plural form of 'child'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Children"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the past tense of 'go'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Went"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the comparative form of 'good'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Better"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the superlative form of 'bad'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Worst"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the synonym of 'happy'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Joyful"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the antonym of 'beautiful'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ugly"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the present continuous form of 'run'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Running"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the past participle of 'write'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Written"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the adjective form of 'beauty'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Beautiful"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the adverb form of 'quick'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Quickly"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the noun form of 'decide'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Decision"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the correct article to use before 'hour'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("An"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the correct pronoun to replace 'John and I'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("We"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the correct form of the verb in the sentence 'She ___ (to be) happy'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("is"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the plural form of 'mouse'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mice"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the past tense of 'teach'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Taught"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the comparative form of 'little'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Less"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the superlative form of 'many'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Most"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the synonym of 'big'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Large"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the antonym of 'easy'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Difficult"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the present continuous form of 'swim'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Swimming"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the past participle of 'eat'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Eaten"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the adjective form of 'anger'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Angry"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the adverb form of 'slow'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Slowly"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the noun form of 'improve'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Improvement"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the correct article to use before 'university'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the correct pronoun to replace 'Sarah and Tom'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("They"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the correct form of the verb in the sentence 'They ___ (to be) ready'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("are"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the plural form of 'foot'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Feet"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the past tense of 'sing'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sang"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the comparative form of 'happy'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Happier"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the superlative form of 'small'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Smallest"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the synonym of 'begin'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Start"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the antonym of 'dark'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Light"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the present continuous form of 'read'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Reading"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the past participle of 'see'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Seen"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the adjective form of 'luck'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Lucky"), outputs=txt)

    
#uiuiui

    with gr.Row():
        gr.Markdown("**What is the name of the city discovered in the Indus Valley Civilization?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mohenjo-Daro"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient city is known for its hanging gardens?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Babylon"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient structure is known as one of the Seven Wonders of the Ancient World and is located in Egypt?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Great Pyramid of Giza"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient city buried by the eruption of Mount Vesuvius in 79 AD?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pompeii"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization built Machu Picchu?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Inca Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient city known for its massive stone heads carved by the Olmec civilization?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("La Venta"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient city is often called the 'Lost City of the Incas'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Machu Picchu"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which archaeological site in Greece is known as the birthplace of the Olympic Games?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Olympia"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient Roman city that was destroyed and buried by the eruption of Mount Vesuvius?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pompeii"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the archaeological site in Peru that contains large geoglyphs best seen from the air?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Nazca Lines"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which famous stone structure in England is believed to have been constructed between 3000 BC to 2000 BC?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Stonehenge"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for its pyramids and hieroglyphs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Egypt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which Mesoamerican civilization is famous for its stepped pyramids, such as El Castillo at Chichen Itza?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Maya Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient Mesopotamian city-state famous for the Code of Hammurabi?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Babylon"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which site in Turkey is considered one of the world's oldest known cities?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Çatalhöyük"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the archaeological site in Jordan that is famous for its rock-cut architecture?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Petra"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for the construction of the Parthenon?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient Roman amphitheater that could hold up to 80,000 spectators?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Colosseum"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the large stone sculpture depicting a reclining feline found in the ruins of Chavín de Huantar in Peru?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Lanzón"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization built the city of Tikal in present-day Guatemala?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Maya Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient city known as the capital of the Minoan civilization on the island of Crete?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Knossos"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient trade route that connected the East and West, facilitating cultural and commercial exchange?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Silk Road"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient city is known for its oracle and was a major site for the worship of the Greek god Apollo?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Delphi"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient capital of the Khmer Empire, known for its temple complex Angkor Wat?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Angkor"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is credited with the invention of writing, specifically cuneiform script?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient structure in Rome that was originally built as a temple for all the gods of ancient Rome?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Pantheon"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which archaeological site in England is believed to have been used for ceremonies and burial grounds?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Stonehenge"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient city in Mexico is known for its massive pyramids, including the Pyramid of the Sun?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Teotihuacan"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the ancient Inca city located in the Andes Mountains of Peru?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Machu Picchu"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for its terracotta army found near the tomb of its first emperor?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Qin Dynasty of China"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient structure in Greece was used for religious festivals, games, and sacrifices?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Parthenon"), outputs=txt)


#pppoppo   

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for its pyramids and pharaohs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Egypt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is credited with the creation of democracy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization built the Colosseum in Rome?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Roman Empire"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What civilization is known for its cuneiform writing system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is associated with the ruins of Machu Picchu?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Inca Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which Mesoamerican civilization is famous for its calendar and pyramids?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Maya Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization built the Great Wall of China?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Chinese Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What civilization is known for its large stone heads and early Mesoamerican culture?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Olmec Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for the epic poem, the Iliad?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What ancient civilization is known for its elaborate hieroglyphics and tombs in the Valley of the Kings?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Egypt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is famous for the Code of Hammurabi, one of the earliest legal codes?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Babylonian Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is associated with the city of Tenochtitlan?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Aztec Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for the Hanging Gardens, one of the Seven Wonders of the Ancient World?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Babylonian Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization developed the first known alphabet?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Phoenician Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for the construction of Angkor Wat?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Khmer Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for its advanced city planning and drainage systems in the Indus Valley?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Harappan Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What civilization is known for the Parthenon and the philosophy of Socrates, Plato, and Aristotle?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is known for its epic literature, such as the Epic of Gilgamesh?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization was ruled by pharaohs and built monumental pyramids and temples along the Nile River?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Egypt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is known for the construction of the ziggurats, large terraced structures?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is credited with the invention of paper?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Chinese Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the civilization that built the Acropolis in Athens?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for the Oracle of Delphi?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Greece"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is known for the mythological labyrinth and the Minotaur?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Minoan Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is associated with the legendary king Gilgamesh?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for building the Hanging Gardens of Babylon?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Babylonian Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization built the Palace of Knossos?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Minoan Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which civilization is known for the invention of the wheel?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for the Rosetta Stone, which helped decipher Egyptian hieroglyphs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ancient Egypt"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the civilization known for the Epic of Gilgamesh?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for its road system that connected its vast empire in South America?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Inca Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization is known for its advanced knowledge of astronomy and mathematics, including the concept of zero?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Maya Civilization"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ancient civilization built the Ziggurat of Ur?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Sumerians"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of adding the matrices A = [[1, 2], [3, 4]] and B = [[2, 1], [1, 2]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[3, 3], [4, 6]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of subtracting the matrices A = [[5, 8], [2, 4]] and B = [[3, 6], [1, 2]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[2, 2], [1, 2]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of multiplying the scalar 3 and the matrix A = [[1, 2], [3, 4]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[3, 6], [9, 12]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of multiplying the matrices A = [[1, 2, 3], [4, 5, 6]] and B = [[7, 8], [9, 10], [11, 12]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[58, 64], [139, 154]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of transposing the matrix A = [[1, 2], [3, 4], [5, 6]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[1, 3, 5], [2, 4, 6]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of finding the determinant of the matrix A = [[3, 1], [2, 4]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("10"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of finding the inverse of the matrix A = [[1, 2], [3, 4]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[-2, 1], [1.5, -0.5]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of raising the matrix A = [[1, 2], [3, 4]] to the power of 2?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[7, 10], [15, 22]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of element-wise multiplication of matrices A = [[1, 2], [3, 4]] and B = [[2, 2], [2, 2]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[2, 4], [6, 8]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of adding the matrices A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[10, 10, 10], [10, 10, 10], [10, 10, 10]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of subtracting the matrices A = [[4, 5], [6, 7]] and B = [[1, 2], [3, 4]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[3, 3], [3, 3]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of multiplying the scalar 2 and the matrix A = [[2, 3], [4, 5]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[4, 6], [8, 10]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of multiplying the matrices A = [[1, 2, 3], [4, 5, 6]] and B = [[7, 8], [9, 10], [11, 12]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[58, 64], [139, 154]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of transposing the matrix A = [[1, 2], [3, 4], [5, 6]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[1, 3, 5], [2, 4, 6]]"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of finding the determinant of the matrix A = [[3, 1], [2, 4]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("10"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the result of finding the inverse of the matrix A = [[1, 2], [3, 4]]?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("[[-2, 1], [1.5, -0.5]]"), outputs=txt)

#fff

    with gr.Row():
        gr.Markdown("**Which ocean is the largest and deepest on Earth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pacific Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is the smallest and shallowest among the five?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Arctic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the deepest point in the ocean and which ocean is it located in?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mariana Trench, Pacific Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is named after the mythical Titan who ruled the sea?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for the scientific study of oceans, including their properties, structure, and behavior?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Oceanography"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is known for the presence of the Great Barrier Reef?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Coral Sea (part of the Pacific Ocean)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a large area of saltwater that is partially enclosed by land?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sea"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is the saltiest?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a body of water surrounded by land on all sides?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Lake"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is home to the largest coral reef system in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pacific Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for the continuous body of saltwater that covers approximately 71% of the Earth's surface?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is located between North and South America?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a large, relatively still body of saltwater that is connected to an ocean?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sea"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is the saltiest?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a body of water surrounded by land on all sides?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Lake"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is home to the largest coral reef system in the world?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pacific Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for the continuous body of saltwater that covers approximately 71% of the Earth's surface?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is located between North and South America?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a large, relatively still body of saltwater that is connected to an ocean?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sea"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is known for the presence of the Ring of Fire, an area with a high degree of tectonic activity?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pacific Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a narrow strip of land that connects two larger landmasses and separates two bodies of water?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Isthmus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is named after the mythical Titan who ruled the sea in Greek mythology?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a large, fast-flowing body of water that is often found in coastal regions?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Current"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which ocean is home to the Sargasso Sea, known for its floating masses of Sargassum seaweed?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Atlantic Ocean"), outputs=txt)


#nnnnn

    with gr.Row():
        gr.Markdown("**Which video game franchise features a plumber named Mario?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Super Mario"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the highest-selling video game of all time?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Minecraft"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which game is known for its blocky, pixelated graphics and open-world sandbox gameplay?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Minecraft"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main protagonist in the Legend of Zelda series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Link"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which video game franchise features a character named Master Chief?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Halo"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the objective of the game Fortnite?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To be the last player or team standing"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which game introduced the concept of capturing and training creatures called Pokémon?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Pokémon"), outputs=txt)

    with gr.Row():
        gr.Markdown("**In which video game series would you find the character Solid Snake?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Metal Gear Solid"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the primary goal of the game Grand Theft Auto (GTA)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To complete missions and explore an open-world environment"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which video game franchise is set in the fictional universe of Azeroth?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("World of Warcraft"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character in the Sonic the Hedgehog series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Sonic"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which game is known for its battle royale mode, where 100 players compete to be the last one standing?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Fortnite"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character in the Assassin's Creed series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Altair (in the first game), Ezio Auditore (in subsequent games)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which video game franchise features a protagonist named Lara Croft?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tomb Raider"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the objective of the game Minecraft?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To survive, build, and explore"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which game features a battle royale mode called Warzone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Call of Duty"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the primary goal of the game The Legend of Zelda?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To rescue Princess Zelda and defeat the main antagonist, usually Ganon or Ganondorf"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which video game series is known for its extensive lore and complex storylines?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Final Fantasy"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the primary antagonist in the Mario series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Bowser"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which game features a main character named Kratos, who seeks revenge against the gods of Olympus?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("God of War"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the primary objective of the game Animal Crossing?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("To create and maintain a virtual community of anthropomorphic animals"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which video game franchise features characters such as Scorpion, Sub-Zero, and Raiden?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mortal Kombat"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character in the Half-Life series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Gordon Freeman"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which game is known for its block-building, construction, and survival mechanics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Minecraft"), outputs=txt)

#jjjjkkkkkkk


    with gr.Row():
        gr.Markdown("**What does 'URL' stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Uniform Resource Locator"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which computer network connects devices within a limited area, such as a home, school, or office building?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Local Area Network (LAN)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("IP Address"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the protocol used to transfer web pages over the Internet?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("HTTP (Hypertext Transfer Protocol)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does 'HTML' stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hypertext Markup Language"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a software application that retrieves and displays content from the World Wide Web?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Web Browser"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which computer network covers a large geographical area, such as a city, country, or continent?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Wide Area Network (WAN)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a unique identifier assigned to network interfaces for communications within a network segment?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("MAC Address"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which computer network connects devices over a large geographic area, often using public telecommunications networks?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Wide Area Network (WAN)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does 'ISP' stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Internet Service Provider"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which protocol is used to send emails over the Internet?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("SMTP (Simple Mail Transfer Protocol)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a standardized system of rules governing the exchange or transmission of data between devices?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Protocol"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which company operates the largest search engine on the Internet?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Google"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does 'HTML' stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hypertext Markup Language"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a unique identifier assigned to network interfaces for communications within a network segment?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("MAC Address"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which computer network connects devices over a large geographic area, often using public telecommunications networks?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Wide Area Network (WAN)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does 'ISP' stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Internet Service Provider"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which protocol is used to send emails over the Internet?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("SMTP (Simple Mail Transfer Protocol)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a standardized system of rules governing the exchange or transmission of data between devices?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Protocol"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which company operates the largest search engine on the Internet?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Google"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a network of servers that deliver content to users based on their geographic location?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Content Delivery Network (CDN)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which organization is responsible for assigning IP addresses and managing the domain name system (DNS)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Internet Corporation for Assigned Names and Numbers (ICANN)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the term for a web page that is generated in response to a user's search query?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Search Engine Results Page (SERP)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which technology allows users to access and use computer programs or applications that are hosted on remote servers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cloud Computing"), outputs=txt)

#llljkkjk

    with gr.Row():
        gr.Markdown("**What is the distance between the Milky Way and the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 2.537 million light-years"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which type of galaxy is the Andromeda Galaxy classified as?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Spiral galaxy"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the approximate diameter of the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("About 220,000 light-years"), outputs=txt)

    with gr.Row():
        gr.Markdown("**When was the Andromeda Galaxy first observed?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Around 964 AD by the Persian astronomer Abd al-Rahman al-Sufi"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Andromeda Galaxy's designation in the New General Catalogue (NGC)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("NGC 224"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the galaxy group that includes the Milky Way and the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Local Group"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which astronomer first proposed that the Andromeda Nebula is actually a distant galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Edwin Hubble"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the approximate number of stars in the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Around 1 trillion stars"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the bright central region of the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda's nucleus or bulge"), outputs=txt)

    with gr.Row():
        gr.Markdown("**How many satellite galaxies does the Andromeda Galaxy have?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Over 20 satellite galaxies"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the common name for the stream of stars pulled from smaller galaxies by the gravitational force of the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda's stellar halo or tidal stream"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which constellation is the Andromeda Galaxy located in?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda constellation"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the bright, star-like nucleus at the center of the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda's core or nucleus"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the approximate mass of the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Approximately 1.5 trillion solar masses"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the largest known globular cluster in the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Mayall II (G1)"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the satellite galaxy of the Andromeda Galaxy discovered in 1998?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda I"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the supermassive black hole at the center of the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda's central black hole or M31*"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which galaxy is the Andromeda Galaxy most often compared to due to its similarity in size and structure?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Milky Way Galaxy"), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the diffuse, extended halo of stars surrounding the Andromeda Galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Andromeda's stellar halo"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which observation method provided crucial evidence that the Andromeda Nebula is a separate galaxy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cepheid variable stars used as distance indicators by Edwin Hubble"), outputs=txt)

#cvcv

    with gr.Row():
        gr.Markdown("**What is machine learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Machine learning is the study of algorithms and statistical models that computer systems use to perform a specific task without using explicit instructions, relying on patterns and inference instead."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What are the main types of machine learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main types of machine learning are supervised learning, unsupervised learning, and reinforcement learning."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Explain supervised learning.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Supervised learning is a type of machine learning where the algorithm is trained on labeled data, and it learns to make predictions from the input-output pairs."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Give an example of supervised learning.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Classification tasks like email spam detection, where the algorithm learns to classify emails as spam or not spam based on labeled training data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Explain unsupervised learning.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Unsupervised learning is a type of machine learning where the algorithm is trained on unlabeled data, and it learns to find patterns and structures in the data without explicit guidance."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Give an example of unsupervised learning.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Clustering tasks like customer segmentation, where the algorithm groups similar customers together based on their purchasing behavior without any predefined labels."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Explain reinforcement learning.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Reinforcement learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative rewards."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Give an example of reinforcement learning.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Training an AI agent to play video games, where the agent learns to maximize its score by taking different actions in the game environment."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the difference between regression and classification?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Regression is used for predicting continuous values, while classification is used for predicting discrete labels or categories."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Name a popular algorithm used for regression.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Linear Regression"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Name a popular algorithm used for classification.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Logistic Regression, Decision Trees, Random Forest, Support Vector Machines (SVM), k-Nearest Neighbors (kNN), etc."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is overfitting in machine learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Overfitting occurs when a model learns the training data too well, capturing noise and irrelevant patterns, leading to poor performance on unseen data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**How can overfitting be prevented?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Overfitting can be prevented by using techniques like cross-validation, regularization, early stopping, and collecting more training data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is underfitting in machine learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Underfitting occurs when a model is too simple to capture the underlying structure of the data, resulting in poor performance both on the training and test data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**How can underfitting be addressed?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Underfitting can be addressed by using more complex models, adding more features, or reducing regularization."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is cross-validation?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Cross-validation is a technique used to evaluate the performance of machine learning models by splitting the data into multiple subsets and training the model on different combinations of these subsets."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of feature scaling in machine learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Feature scaling is used to standardize or normalize the range of independent variables or features in the data, preventing features with large values from dominating the learning process."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Name a popular algorithm used for clustering.**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("k-Means Clustering, Hierarchical Clustering, DBSCAN, Gaussian Mixture Models (GMM), etc."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the curse of dimensionality in machine learning?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The curse of dimensionality refers to the phenomenon where the performance of machine learning algorithms degrades as the number of features or dimensions in the data increases, leading to sparsity and computational inefficiency."), outputs=txt)



#ghghggh



    with gr.Row():
        gr.Markdown("**What is GitHub?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("GitHub is a web-based platform used for version control and collaboration on software development projects."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is version control?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Version control is a system that records changes to files over time, allowing you to track and manage different versions of your codebase."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Git?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Git is an open-source distributed version control system used to track changes in source code during software development."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a repository in GitHub?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A repository, or repo, is a storage space where your project's files and revision history are stored."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a commit in Git?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A commit is a snapshot of your repository at a specific point in time. It records changes made to the files in your project."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a pull request?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A pull request is a way to propose changes to a repository in GitHub. It allows you to notify others about the changes you've made and request their review and feedback."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is forking in GitHub?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Forking is the process of creating a personal copy of someone else's repository. It allows you to freely experiment with changes without affecting the original project."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a branch in Git?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A branch is a parallel version of your repository's code. It allows you to work on different features or fixes without affecting the main codebase."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a merge conflict?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A merge conflict occurs when Git cannot automatically merge two branches due to conflicting changes in the same file."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Git clone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Git clone is a command used to create a local copy of a remote repository in your local machine."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Git push?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Git push is a command used to upload local repository content to a remote repository on GitHub."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Git pull?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Git pull is a command used to fetch and download changes from a remote repository to your local repository, and immediately update your working directory."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a README.md file?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A README.md file is a text file that contains information about your project. It typically includes a description, installation instructions, usage examples, etc."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a .gitignore file?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A .gitignore file is a text file that specifies intentionally untracked files to be ignored by Git. It prevents these files from being accidentally committed to the repository."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of the Issues tab in GitHub?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Issues tab is used to track tasks, enhancements, and bugs for your projects. It allows users to open, discuss, and close issues related to the project."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Projects tab in GitHub used for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Projects tab is used to organize and prioritize tasks, track progress, and manage workflows for your project. It provides a visual way to plan and manage project work."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Wiki tab in GitHub used for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Wiki tab is used to create and maintain documentation for your project. It allows users to collaboratively write and edit project documentation using Markdown."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a GitHub Action?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A GitHub Action is a workflow automation tool provided by GitHub. It allows you to automate tasks, build, test, and deploy your code directly from GitHub."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a GitHub Gist?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A GitHub Gist is a simple way to share snippets of code or text with others. It allows you to create and share individual files or multiple files as a collection."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of the Insights tab in GitHub?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Insights tab provides statistics and analytics about your project's code, pull requests, and issues. It helps you understand the health and activity of your project."), outputs=txt)

#jjjjjjj

    with gr.Row():
        gr.Markdown("**What is Hugging Face?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hugging Face is an organization that provides state-of-the-art natural language processing (NLP) models, datasets, and libraries through its open-source platform."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is Transformers in Hugging Face?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Transformers is a library built by Hugging Face that provides an easy-to-use interface for working with state-of-the-art NLP models like BERT, GPT, RoBERTa, etc."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What are some popular pre-trained models available in Hugging Face Transformers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Some popular pre-trained models include BERT, GPT, RoBERTa, DistilBERT, T5, XLNet, etc."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a tokenizer in Hugging Face Transformers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A tokenizer is a component in Hugging Face Transformers that is used to convert raw text input into numerical inputs suitable for feeding into a model."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of Hugging Face Datasets?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hugging Face Datasets is a library that provides easy access to a wide range of datasets for natural language processing (NLP) tasks. It allows users to load and preprocess datasets with just a few lines of code."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a pipeline in Hugging Face Transformers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A pipeline is a high-level interface provided by Hugging Face Transformers that allows users to easily perform various NLP tasks such as text generation, text classification, named entity recognition (NER), etc., using pre-trained models."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is a model hub in Hugging Face?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The model hub is a repository hosted by Hugging Face that contains a wide variety of pre-trained models, datasets, and configurations. It allows users to discover, share, and download models and datasets for their NLP tasks."), outputs=txt)

    with gr.Row():
        gr.Markdown("**How can you install Hugging Face Transformers library?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("You can install the Hugging Face Transformers library using pip: `pip install transformers`. Additionally, you can install specific versions or from the source on GitHub."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is fine-tuning in Hugging Face Transformers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Fine-tuning is the process of training a pre-trained model on a specific task or dataset to adapt it to new data or improve its performance on a particular task. It involves modifying the parameters of the model and training it on task-specific data."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is model distillation in Hugging Face Transformers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Model distillation is a process in which a large, complex pre-trained model is used to train a smaller, faster model (student model) by transferring knowledge from the larger model to the smaller one. It aims to retain the performance of the larger model while reducing its size and computational cost."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the Hugging Face Inference API?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Hugging Face Inference API is a cloud-based service provided by Hugging Face that allows users to deploy and run their models in production environments. It provides a simple REST API interface for making predictions using pre-trained models hosted on the Hugging Face model hub."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is zero-shot learning in Hugging Face?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Zero-shot learning is a technique in Hugging Face that allows a model to perform a task without any direct supervision or training data for that specific task. Instead, the model is provided with a description or prompt of the task, and it generates the desired output based on its pre-trained knowledge."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of Hugging Face Trainer?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Hugging Face Trainer is a utility provided by Hugging Face that simplifies the training and evaluation of custom models using pre-trained models from the Transformers library. It handles various training tasks such as batching, gradient accumulation, distributed training, etc., and provides an easy-to-use interface for model training."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is adversarial training in Hugging Face?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Adversarial training is a technique in Hugging Face used to improve the robustness and generalization of models by training them on adversarially perturbed examples. It involves generating small, imperceptible perturbations to input examples and adding them to the training data to make the model more robust to such perturbations during inference."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of Hugging Face Accelerated Inference API?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Hugging Face Accelerated Inference API is a cloud-based service provided by Hugging Face that allows users to deploy and run their models in production environments with optimized performance and scalability. It leverages accelerators such as GPUs and TPUs to accelerate model inference and reduce latency."), outputs=txt)


#vbvbbv


    with gr.Row():
        gr.Markdown("**What is the output of the following Python code snippet?**\n```python\nprint(3 + 4 * 2)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 11. The multiplication operator (*) has higher precedence than the addition operator (+), so 4 * 2 is evaluated first, resulting in 8, and then 3 is added to it."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will the following code snippet output?**\n```python\nx = 'Hello'\nprint(x[::-1])\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 'olleH'. The slicing syntax [::-1] reverses the string 'Hello', resulting in 'olleH'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the output of the following Python code?**\n```python\nx = 5\ny = 2\nprint(x % y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 1. The % operator is the modulus operator, which computes the remainder of the division of x by y."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code?**\n```python\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output will be [1, 2, 3, 4]. When y is assigned to x, it creates a reference to the same list object. Therefore, when y.append(4) is called, it modifies the original list referred to by x."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the output of the following Python code snippet?**\n```python\nx = 10\ny = 3\nprint(x // y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 3. The // operator performs integer division, which returns the quotient of x divided by y, discarding any fractional part."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the output of the following code?**\n```python\nx = [1, 2, 3]\ny = x\ny = y + [4]\nprint(x)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output will be [1, 2, 3]. When y is assigned to x, it creates a reference to the same list object. However, when y = y + [4] is executed, a new list is created, and y is reassigned to this new list, leaving the original list referred to by x unchanged."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will the following code output?**\n```python\nx = 2\ny = 5\nprint(x ** y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 32. The ** operator represents exponentiation, so x ** y is equivalent to 2 raised to the power of 5, which equals 32."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does the following Python code snippet output?**\n```python\nx = 'hello'\nprint(x.capitalize())\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 'Hello'. The capitalize() method in Python returns a copy of the string with its first character capitalized and the rest lowercased."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will be the output of the following code snippet?**\n```python\nx = [1, 2, 3]\nprint(x.pop())\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 3. The pop() method removes and returns the last item from the list x, which is 3 in this case."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the output of the following Python code?**\n```python\nx = 7\ny = 2\nprint(x / y)\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 3.5. In Python 3.x, the division operator (/) performs floating-point division, resulting in a floating-point number."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does the following Python code output?**\n```python\nx = 'hello'\nprint(x.upper())\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 'HELLO'. The upper() method in Python returns a copy of the string with all its characters converted to uppercase."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the output of the following code snippet?**\n```python\nx = [1, 2, 3]\nx.append([4, 5])\nprint(len(x))\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 4. The append() method adds the entire list [4, 5] as a single element to the list x, increasing its length to 4."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What will the following Python code snippet output?**\n```python\nx = 'python'\nprint(x[1:4])\n```")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The output is 'yth'. Python slicing syntax x[1:4] extracts characters from index 1 up to, but not including, index 4 from the string x."), outputs=txt)


#ddrr

    with gr.Row():
        gr.Markdown("**In which fictional city does the game 'Grand Theft Auto: Vice City' take place?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The game 'Grand Theft Auto: Vice City' takes place in the fictional city of Vice City, which is based on Miami, Florida."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the main protagonist of 'Grand Theft Auto: San Andreas'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main protagonist of 'Grand Theft Auto: San Andreas' is Carl 'CJ' Johnson."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which fictional city is the setting for 'Grand Theft Auto IV'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The setting for 'Grand Theft Auto IV' is the fictional Liberty City, which is based on New York City."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character in 'Grand Theft Auto V'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main characters in 'Grand Theft Auto V' are Michael De Santa, Franklin Clinton, and Trevor Philips."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which installment of the 'Grand Theft Auto' series introduced the concept of multiple playable characters?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The concept of multiple playable characters was introduced in 'Grand Theft Auto V', where players can switch between three main characters throughout the game."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the gang led by Big Smoke in 'Grand Theft Auto: San Andreas'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The gang led by Big Smoke in 'Grand Theft Auto: San Andreas' is called the Grove Street Families."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which version of Liberty City does 'Grand Theft Auto: IV' feature?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Grand Theft Auto IV features an updated and more realistic version of Liberty City compared to its earlier appearances in the series."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the biker gang in 'Grand Theft Auto: Vice City'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The biker gang in 'Grand Theft Auto: Vice City' is called the Vice City Bikers."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which city is featured in 'Grand Theft Auto: Chinatown Wars'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The city featured in 'Grand Theft Auto: Chinatown Wars' is Liberty City."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the primary antagonist in 'Grand Theft Auto: San Andreas'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The primary antagonist in 'Grand Theft Auto: San Andreas' is Officer Frank Tenpenny."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character in 'Grand Theft Auto: Liberty City Stories'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character in 'Grand Theft Auto: Liberty City Stories' is Toni Cipriani."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which fictional state is featured in 'Grand Theft Auto: San Andreas'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The fictional state of San Andreas is featured in 'Grand Theft Auto: San Andreas'. It consists of three major cities: Los Santos, San Fierro, and Las Venturas."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the gang led by Sweet in 'Grand Theft Auto: San Andreas'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The gang led by Sweet in 'Grand Theft Auto: San Andreas' is the Grove Street Families."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the protagonist of 'Grand Theft Auto III'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The protagonist of 'Grand Theft Auto III' is Claude."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which 'Grand Theft Auto' game introduced the concept of purchasing properties and businesses?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The concept of purchasing properties and businesses was introduced in 'Grand Theft Auto: Vice City'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the radio station hosted by Lazlow in 'Grand Theft Auto: Vice City'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The radio station hosted by Lazlow in 'Grand Theft Auto: Vice City' is V-Rock."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which fictional city is the setting for 'Grand Theft Auto: III'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The setting for 'Grand Theft Auto: III' is the fictional Liberty City, which is based on New York City"), outputs=txt)

#4444444

    with gr.Row():
        gr.Markdown("**In which year was the original 'Red Dead Redemption' game released?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The original 'Red Dead Redemption' game was released in 2010."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the protagonist of 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The protagonist of 'Red Dead Redemption 2' is Arthur Morgan."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the gang led by Dutch van der Linde in 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The gang led by Dutch van der Linde in 'Red Dead Redemption 2' is called the Van der Linde Gang."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which fictional U.S. state is the setting for 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The setting for 'Red Dead Redemption 2' is the fictional U.S. state of New Hanover, along with other fictional regions resembling real-life states like West Elizabeth and Lemoyne."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character's horse in 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character's horse in 'Red Dead Redemption 2' is named the player's choice, but the default name is 'The Count.'"), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which studio developed the 'Red Dead Redemption' series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The 'Red Dead Redemption' series was developed by Rockstar Games, specifically by its subsidiary Rockstar San Diego."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the protagonist's former gang member in 'Red Dead Redemption 2' who becomes an enemy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The protagonist's former gang member in 'Red Dead Redemption 2' who becomes an enemy is Micah Bell."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What year does 'Red Dead Redemption 2' take place in?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The events of 'Red Dead Redemption 2' take place in 1899."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the primary antagonist in 'Red Dead Redemption'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The primary antagonist in 'Red Dead Redemption' is Edgar Ross."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character's son in 'Red Dead Redemption'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character's son in 'Red Dead Redemption' is named Jack Marston."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the gang that John Marston is hunting down in 'Red Dead Redemption'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The gang that John Marston is hunting down in 'Red Dead Redemption' is Bill Williamson's gang."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the nickname of the main character in 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The nickname of the main character in 'Red Dead Redemption 2' is 'Black Lung,' given to him by other members of the Van der Linde Gang."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the gang that Dutch van der Linde and Arthur Morgan belong to in 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Dutch van der Linde and Arthur Morgan belong to the Van der Linde Gang in 'Red Dead Redemption 2'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which law enforcement agency is John Marston forced to work for in 'Red Dead Redemption'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("John Marston is forced to work for the Bureau of Investigation (BOI) in 'Red Dead Redemption'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the character who serves as the main antagonist in 'Red Dead Redemption 2'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The character who serves as the main antagonist in 'Red Dead Redemption 2' is Leviticus Cornwall."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the character who helps John Marston during his quest in 'Red Dead Redemption'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The character who helps John Marston during his quest in 'Red Dead Redemption' is Landon Ricketts."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which animal serves as the symbol/logo for the 'Red Dead Redemption' series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The American Bison serves as the symbol/logo for the 'Red Dead Redemption' series."), outputs=txt)

#5555555555666

    with gr.Row():
        gr.Markdown("**Who directed the movie 'Inception'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'Inception' was directed by Christopher Nolan."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which actor played the role of Tony Stark/Iron Man in the Marvel Cinematic Universe?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Robert Downey Jr. played the role of Tony Stark/Iron Man in the Marvel Cinematic Universe."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the highest-grossing film of all time (as of 2022)?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("As of 2022, the highest-grossing film of all time is 'Avatar' directed by James Cameron."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which movie won the Academy Award for Best Picture in 2020?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'Parasite' won the Academy Award for Best Picture in 2020."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who played the role of Neo in 'The Matrix' trilogy?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Keanu Reeves played the role of Neo in 'The Matrix' trilogy."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which film is famous for the line: 'Here's looking at you, kid'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The line 'Here's looking at you, kid' is from the movie 'Casablanca' directed by Michael Curtiz."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who directed the movie 'Jurassic Park'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'Jurassic Park' was directed by Steven Spielberg."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which actress won the Academy Award for Best Actress for her role in 'La La Land'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Emma Stone won the Academy Award for Best Actress for her role in 'La La Land'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who directed the movie 'The Dark Knight'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'The Dark Knight' was directed by Christopher Nolan."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which actor played the role of Captain Jack Sparrow in the 'Pirates of the Caribbean' series?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Johnny Depp played the role of Captain Jack Sparrow in the 'Pirates of the Caribbean' series."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who directed the movie 'The Shawshank Redemption'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'The Shawshank Redemption' was directed by Frank Darabont."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which movie features the character Hannibal Lecter?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The character Hannibal Lecter appears in the movie 'The Silence of the Lambs'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who won the Academy Award for Best Actor for his role in 'The Revenant'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Leonardo DiCaprio won the Academy Award for Best Actor for his role in 'The Revenant'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which film won the Academy Award for Best Animated Feature in 2021?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The film 'Soul' won the Academy Award for Best Animated Feature in 2021."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who played the role of Forrest Gump in the movie of the same name?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Tom Hanks played the role of Forrest Gump in the movie of the same name."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which movie features the character Tyler Durden?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The character Tyler Durden appears in the movie 'Fight Club'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who directed the movie 'Schindler's List'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'Schindler's List' was directed by Steven Spielberg."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which actor played the role of Vito Corleone in 'The Godfather'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Marlon Brando played the role of Vito Corleone in 'The Godfather'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who directed the movie 'Forrest Gump'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'Forrest Gump' was directed by Robert Zemeckis."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which movie won the Academy Award for Best Picture in 2019?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The movie 'Green Book' won the Academy Award for Best Picture in 2019."), outputs=txt)

#tttttttrrrrrrrt

    with gr.Row():
        gr.Markdown("**Who is the main character of 'Naruto'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character of 'Naruto' is Naruto Uzumaki."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the giant humanoid creatures in 'Attack on Titan'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The giant humanoid creatures in 'Attack on Titan' are called Titans."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the protagonist of 'One Piece'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The protagonist of 'One Piece' is Monkey D. Luffy."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which anime features a young boy named Gon Freecss on a quest to find his father?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The anime that features Gon Freecss on a quest to find his father is 'Hunter x Hunter'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the female titan in 'Attack on Titan'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The name of the female titan in 'Attack on Titan' is Annie Leonhart."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the creator of 'Dragon Ball'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The creator of 'Dragon Ball' is Akira Toriyama."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which anime follows the adventures of the Elric brothers in search of the Philosopher's Stone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The anime that follows the adventures of the Elric brothers in search of the Philosopher's Stone is 'Fullmetal Alchemist: Brotherhood'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the main character in 'Death Note'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character in 'Death Note' is Light Yagami."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which anime features a group of high school students who possess unique powers called 'Quirks'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The anime that features high school students with 'Quirks' is 'My Hero Academia'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is known as the 'Saiyan Prince' in 'Dragon Ball Z'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The character known as the 'Saiyan Prince' in 'Dragon Ball Z' is Vegeta."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the virtual reality world in 'Sword Art Online'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The virtual reality world in 'Sword Art Online' is called Aincrad."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the main character of 'One Punch Man'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character of 'One Punch Man' is Saitama."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the organization that trains assassins in 'Assassination Classroom'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The organization that trains assassins in 'Assassination Classroom' is called the Kunugigaoka Junior High School."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the main character in 'Attack on Titan'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character in 'Attack on Titan' is Eren Yeager."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the demon fox sealed within Naruto in 'Naruto'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The name of the demon fox sealed within Naruto in 'Naruto' is Kurama."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the creator of 'Naruto'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The creator of 'Naruto' is Masashi Kishimoto."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which anime follows the journey of Edward and Alphonse Elric to restore their bodies after a failed alchemical experiment?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The anime that follows the journey of Edward and Alphonse Elric is 'Fullmetal Alchemist'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the floating city in 'Castle in the Sky'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The name of the floating city in 'Castle in the Sky' is Laputa."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Who is the main character of 'Dragon Ball'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The main character of 'Dragon Ball' is Goku."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which anime features a young ninja named Asta striving to become the Wizard King?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The anime that features a young ninja named Asta striving to become the Wizard King is 'Black Clover'."), outputs=txt)

#gvgvvvv


    with gr.Row():
        gr.Markdown("**What is the largest organ in the human body?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The largest organ in the human body is the skin."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the tube that connects the mouth to the stomach?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The tube that connects the mouth to the stomach is the esophagus."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which blood type is known as the 'universal donor'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Blood type O negative is known as the 'universal donor'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for high blood pressure?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for high blood pressure is hypertension."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which part of the brain controls balance and coordination?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The cerebellum, located at the back of the brain, controls balance and coordination."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the voice box?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the voice box is the larynx."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the name of the longest bone in the human body?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The longest bone in the human body is the femur."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which gland in the human body regulates metabolism?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The thyroid gland regulates metabolism."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the thigh bone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the thigh bone is the femur."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which part of the human eye is responsible for central vision?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The macula, located in the retina, is responsible for central vision."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the collarbone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the collarbone is the clavicle."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which hormone is known as the 'stress hormone'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The hormone known as the 'stress hormone' is cortisol."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the kneecap?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the kneecap is the patella."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which organ in the human body produces insulin?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The pancreas produces insulin."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the shoulder blade?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the shoulder blade is the scapula."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which part of the human brain controls voluntary movements and coordination?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The cerebellum, located at the back of the brain, controls voluntary movements and coordination."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the windpipe?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the windpipe is the trachea."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which blood type is known as the 'universal recipient'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Blood type AB positive is known as the 'universal recipient'."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the thigh bone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the thigh bone is the femur."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which part of the human eye contains cells that detect light and color?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The retina, located at the back of the eye, contains cells that detect light and color."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the medical term for the wrist bone?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The medical term for the wrist bone is the carpal."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which gland in the human body is often referred to as the 'master gland'?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The pituitary gland is often referred to as the 'master gland'."), outputs=txt)

#tttyyyy

    with gr.Row():
        gr.Markdown("**Which company manufactures the Ryzen series of CPUs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Ryzen series of CPUs is manufactured by AMD (Advanced Micro Devices)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does CPU stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("CPU stands for Central Processing Unit."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which CPU architecture is used in most modern desktop computers?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Most modern desktop computers use x86 CPU architecture."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of the GPU in a computer system?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The GPU (Graphics Processing Unit) is primarily responsible for rendering images and graphics in a computer system."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which company manufactures the GeForce series of GPUs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The GeForce series of GPUs is manufactured by NVIDIA."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of the CPU cache?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The CPU cache is used to store frequently accessed data and instructions to speed up processing."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which CPU socket type is commonly used for Intel processors?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The LGA (Land Grid Array) socket type is commonly used for Intel processors."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of overclocking a CPU?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Overclocking a CPU involves increasing its clock speed beyond the manufacturer's specifications to achieve higher performance."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which CPU feature allows it to execute multiple threads simultaneously?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Hyper-Threading (HT) is a CPU feature that allows it to execute multiple threads simultaneously."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the primary function of the ALU in a CPU?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The ALU (Arithmetic Logic Unit) is responsible for performing arithmetic and logical operations in a CPU."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which CPU architecture is commonly used in mobile devices such as smartphones and tablets?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("ARM (Advanced RISC Machine) architecture is commonly used in mobile devices such as smartphones and tablets."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the function of the GPU's VRAM?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The GPU's VRAM (Video Random Access Memory) is dedicated memory used to store textures, frame buffers, and other graphics data for rendering images and graphics on a display device."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which technology allows multiple GPUs to work together to improve graphics performance?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("SLI (Scalable Link Interface) and CrossFire are technologies that allow multiple GPUs to work together to improve graphics performance."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What does GPU stand for?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("GPU stands for Graphics Processing Unit."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which company manufactures the Radeon series of GPUs?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Radeon series of GPUs is manufactured by AMD (Advanced Micro Devices)."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of a GPU cooler?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("A GPU cooler is used to dissipate heat generated by the GPU during operation to prevent overheating and maintain optimal performance."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which GPU architecture is used in NVIDIA's RTX series of graphics cards?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("The Turing architecture is used in NVIDIA's RTX series of graphics cards."), outputs=txt)

    with gr.Row():
        gr.Markdown("**What is the purpose of GPU rendering?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("GPU rendering utilizes the GPU's parallel processing capabilities to accelerate the rendering of images and graphics, particularly in 3D applications and games."), outputs=txt)

    with gr.Row():
        gr.Markdown("**Which GPU feature is responsible for simulating realistic lighting effects in computer graphics?**")
        btn = gr.Button("Show Answer")
        txt = gr.Textbox()
        btn.click(fn=lambda: display_answer("Ray tracing is a GPU feature that simulates realistic lighting effects in computer graphics ."), outputs=txt)

    
        
demo.launch()