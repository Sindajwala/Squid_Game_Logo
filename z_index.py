from manim import*

class zindex(Scene):
    def construct(self):
        square1 = Square(side_length=2, stroke_width=15, color=BLUE).set_fill(GREEN, opacity=0.8).shift(UP*1.5+LEFT*3.5).set_z_index(8)
        square2 = Square(side_length=2, stroke_width=15,color=YELLOW).set_fill(BLUE, opacity=0.8).shift(UP*2,LEFT*3).set_z_index(9)
        square3 = Square(side_length=2, stroke_width=15).set_fill(RED, opacity=0.8).shift(UP*2.5,LEFT*2.5).set_z_index(10)
        text1 = Text("z=index=1").next_to(square1,DOWN*0.75+RIGHT*0.5).scale(0.5)
        text2 = Text("z=index=2").next_to(square2,DOWN*0.75+RIGHT*0.5).scale(0.5)
        text3 = Text("z=index=3").next_to(square3,DOWN*0.75+RIGHT*0.5).scale(0.5)
        
        square4 = Square(side_length=2, stroke_width=15,color=BLUE).set_fill(GREEN, opacity=0.8).shift(DOWN*1.5+RIGHT*2.5).set_z_index(10)
        square5 = Square(side_length=2, stroke_width=15,color=YELLOW).set_fill(BLUE, opacity=0.8).shift(DOWN*2,RIGHT*3).set_z_index(9)
        square6 = Square(side_length=2, stroke_width=15).set_fill(RED, opacity=0.8).shift(DOWN*2.5,RIGHT*3.5).set_z_index(8)
        text4 = Text("z=index=3").next_to(square4,UP*0.75+RIGHT*0.5).scale(0.5)
        text5 = Text("z=index=2").next_to(square5,UP*0.75+RIGHT*0.5).scale(0.5)
        text6 = Text("z=index=1").next_to(square6,UP*0.75+RIGHT*0.5).scale(0.5)

        #Arrow

        arrow_1 = Arrow(start=LEFT*2+UP*0.2, end=UP*2, color=GOLD)
        arrow_2 = Arrow(start=RIGHT*3.5, end=RIGHT*5.5+DOWN*1.5)

        self.play(Succession(Succession(FadeIn(square1),AddTextLetterByLetter(text1)),
                  Succession(FadeIn(square2),AddTextLetterByLetter(text2)),
                  Succession(FadeIn(square3),AddTextLetterByLetter(text3)),
                  Create(arrow_1)),
                  
        )
        self.wait()

        self.play(Succession(Succession(FadeIn(square4),AddTextLetterByLetter(text4)),
                  Succession(FadeIn(square5),AddTextLetterByLetter(text5)),
                  Succession(FadeIn(square6),AddTextLetterByLetter(text6)),
                  Create(arrow_2)),
                  
        )

        # self.add(square1,square2,square3,text1,text2,text3,square4,square5,square6,text4,text5,text6,arrow_1,arrow_2)
        # self.wait()
