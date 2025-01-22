from manim import *

class logo(Scene):
    def construct(self):

        # Define the shapes
        up_circle = Arc(radius=0.6, angle=PI * 2, start_angle=1.5708, stroke_width=22).shift(UP * 2.8)
        triangle = Triangle(stroke_width=22, stroke_color=WHITE).shift(UP * 1.3).scale(1.5)
        line_t1 = Line(start=[-1.4, 0, 0], end=[1.4, 0, 0], stroke_width=15).shift(UP * 0.4)
        down_circle = Arc(radius=0.6, angle=PI * 2, start_angle=270 * DEGREES, stroke_width=22).shift(DOWN * 2.8)
        line_1h = Line(start=[-1.5, 0, 0], end=[1.5, 0, 0], stroke_width=22)
        line_2v = Line(start=[-1.4, 1.5, 0], end=[-1.4, -1.5, 0], stroke_width=22).shift(DOWN * 1.4)
        line_3v = Line(start=[1.4, 1.5, 0], end=[1.4, -1.5, 0], stroke_width=22).shift(DOWN * 1.4)
        line_4h = Line(start=[-1.5, 0, 0], end=[1.5, 0, 0], stroke_width=22).shift(DOWN * 2.8)

         # First  Symbols appearance
        self.play(FadeIn(up_circle, down_circle, triangle, line_1h, line_2v, line_3v, line_4h, line_t1))
        self.wait(1)

    #     #Transformation of previous lines
    #     line_1h.generate_target()
    #     line_1h.target.shift(3.5*RIGHT).scale(0.075)
    #     line_1h_ch1 = Line(start=[3.5,0,0], end=[3.5,-0.7,0],stroke_width=22)

    #     line_2v.generate_target()
    #     line_2v.target.shift(0.7*UP).scale(0.075)
    #     line_2v_ch1 = Line(start=[-1.5,-0.7,0], end=[1,-0.7,0], stroke_width = 22)
    #     line_2v_ch1.generate_target()
    #     line_2v_ch1.target.shift(3.33*RIGHT).scale(0.42)

    #     line_3v.generate_target()
    #     line_3v.target.shift(1.6*UP).scale(0.075)
    #     line_3_ch1 = Line(start=[1.37,0.2,0], end=[2.4,0.2,0], stroke_width=22)
    #     line_3_ch1.generate_target()
    #     line_3_ch1.target.shift(1.21*RIGHT)
       
    #     line_4h.generate_target()
    #     line_4h.target.shift(2.6*RIGHT).scale(0.075)
    #     line_4_ch1 = Line(start=[2.65,-2.8,0], end=[2.65,-1.7,0], stroke_width=22)
    #     line_4_ch1.generate_target()
    #     line_4_ch1.target.shift(2*UP)

    #    #1st Transformation of Previous Triangle
    #     triangle.generate_target()
    #     triangle.target.shift(1*RIGHT + 0.85*DOWN).scale(0.25)

    #     self.play(Succession(MoveToTarget(line_1h),Create(line_1h_ch1)),
    #               MoveToTarget(line_2v),
    #               MoveToTarget(line_3v),
    #               MoveToTarget(line_4h),
    #               MoveToTarget(triangle),
    #               )
        
    #     triangle.generate_target()
    #     triangle.target.shift(2.8*LEFT)

    #     self.play(
    #               Create(line_3_ch1),
    #               FadeOut(line_3v, shift=RIGHT),
    #               MoveToTarget(line_3_ch1),
    #               Create(line_2v_ch1),
    #               FadeOut(line_2v, shift=RIGHT),
    #               Create(line_4_ch1),
    #               FadeOut(line_4h,shift=UP),
    #               MoveToTarget(triangle),
    #               Uncreate(line_t1),
    #              )
    #     self.wait()
      
        #     #UpCircle Animation
        # line_upc1 = Line(start=[-0.1,3.4,0], end=[3,3.4,0], stroke_width=22)
        # line_upc1.generate_target()
        # line_upc1.target.shift(1.5*RIGHT).scale(0.07)

        # self.play(Uncreate(up_circle),
        #           Create(line_upc1))
        # self.play(MoveToTarget(line_upc1))
        # line_upc2 = Line(start=[2.9,3.5,0], end=[2.9,1,0], stroke_width=22)
        # self.play(Uncreate(line_upc1),
        #            Create(line_upc2))
        # line_upc2.generate_target()
        # line_upc2.target.shift(1.2*DOWN).scale(0.1)
        # up_circle2 = Arc(radius=0.3,angle=-PI *2, start_angle=360*DEGREES, stroke_width=22).shift(2.6*RIGHT + UP*1)
        
        # self.play(Create(up_circle2),
        #           MoveToTarget(line_upc2))

         #DownCircle Animation
        line_dc1 = Line (start=[0.1,-3.4,0], end=[-3,-3.4,0], stroke_width=22)
        line_dc1.generate_target()
        line_dc1.target.shift(1.6*LEFT).scale(0.07)
        self.play(Uncreate(down_circle),
                  Create(line_dc1))
        self.play(MoveToTarget(line_dc1))
        line_dc2 = Line(start=[-3.05,-3.4,0], end=[-3.05,1.2,0], stroke_width=22)
        self.play(Uncreate(line_dc1),
                   Create(line_dc2))
        line_dc2.generate_target()
        line_dc2.target.shift(2.2*UP).scale(0.01)
        down_circle2 = Arc(radius=0.3,angle=PI *2, start_angle=360*DEGREES, stroke_width=22).shift(3.35*LEFT + UP*1.1)
        self.play(Create(down_circle2),
                  MoveToTarget(line_dc2))
