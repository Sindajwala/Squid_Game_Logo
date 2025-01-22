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
        #square = Square(side_length=2.9, stroke_width=20).shift(DOWN*1.4)

        # First  Symbols appearance
        self.play(FadeIn(up_circle, down_circle, triangle, line_1h, line_2v, line_3v, line_4h, line_t1))
        #self.remove(square)
        self.wait(1)

        # Appearance of new lines
        line_5h = Line(start=[-2.7, -0.35, 0], end=[-4.4, -0.35, 0], stroke_width=22).shift(UP * 0.5)
        line_6v = Line(start=[-1, 1.8, 0], end=[-1, 0.5, 0], stroke_width=22)
        line_7v = Line(start=[1.5, -1, 0], end=[1.5, 0.25, 0], stroke_width=22)
        line_8v = Line(start=[1, 1.8, 0], end=[1, 0.5, 0], stroke_width=22)
        line_9h = Line(start=[-2.3, 1.2, 0], end=[-1.4, 1.2, 0], stroke_width=22)
        line_10v = Line(start=[2, -1.5, 0], end=[2, 0.25, 0], stroke_width=22)
        line_11v = Line(start=[-3.35, 0.1, 0], end=[-3.35, 0.8, 0], stroke_width=22)
        line_12h = Line(start=[1, 1.1, 0], end=[0, 1.1, 0], stroke_width=22)
        line_13h = Line(start=[0.4, 0.13, 0], end=[1.2, 0.13, 0], stroke_width=22)
        line_14 = Line(start=[0.4, -1, 0], end=[1.1, 0.135, 0], stroke_width=22)
        line_15h = Line(start=[0.75, -0.3, 0], end=[1.5, -0.3, 0], stroke_width=22)
        line_16v = Line(start=[3.5,2,0],end=[3.5,0.5,0], stroke_width=22)
         #lines related to up/down circles transformation
        line_upc1 = Line(start=[-0.1,3.4,0], end=[3,3.4,0], stroke_width=22)
        line_upc1.generate_target()
        line_upc1.target.shift(1.5*RIGHT).scale(0.07)
        line_dc1 = Line (start=[0.1,-3.4,0], end=[-3,-3.4,0], stroke_width=22)
        line_dc1.generate_target()
        line_dc1.target.shift(1.6*LEFT).scale(0.07)
        
        line_upc2 = Line(start=[2.9,3.5,0], end=[2.9,1,0], stroke_width=22)
        line_dc2 = Line(start=[-3.05,-3.4,0], end=[-3.05,1.2,0], stroke_width=22)
       
        up_circle2 = Arc(radius=0.3,angle=-PI *2, start_angle=360*DEGREES, stroke_width=22).shift(2.6*RIGHT + UP*1)
        
        down_circle2 = Arc(radius=0.3,angle=PI *2, start_angle=360*DEGREES, stroke_width=22).shift(3.35*LEFT + UP*1.1)

        #Transformation of previous lines
        line_1h.generate_target()
        line_1h.target.shift(3.5*RIGHT).scale(0.075)
        line_1h_ch1 = Line(start=[3.5,0,0], end=[3.5,-0.7,0],stroke_width=22)

        line_2v.generate_target()
        line_2v.target.shift(0.7*UP).scale(0.075)
        line_2v_ch1 = Line(start=[-1.5,-0.7,0], end=[1,-0.7,0], stroke_width = 22)
        line_2v_ch1.generate_target()
        line_2v_ch1.target.shift(3.33*RIGHT).scale(0.42)

        line_3v.generate_target()
        line_3v.target.shift(1.6*UP).scale(0.075)
        line_3_ch1 = Line(start=[1.37,0.2,0], end=[2.4,0.2,0], stroke_width=22)
        line_3_ch1.generate_target()
        line_3_ch1.target.shift(1.21*RIGHT)
       
        line_4h.generate_target()
        line_4h.target.shift(2.6*RIGHT).scale(0.075)
        line_4_ch1 = Line(start=[2.65,-2.8,0], end=[2.65,-1.7,0], stroke_width=22)
        line_4_ch1.generate_target()
        line_4_ch1.target.shift(2*UP)

       #1st Transformation of Previous Triangle
        triangle.generate_target()
        triangle.target.shift(1*RIGHT + 0.85*DOWN).scale(0.25)
              
        #2nd Transformation
              
        #Appearance of new Shapes
        circle_2 = Annulus(inner_radius=0.001, outer_radius=0.002).shift(1.5*LEFT+0.25*DOWN)
        circle_2_ch1= Annulus(inner_radius=0.2, outer_radius= 0.4).shift(1.5*LEFT+0.25*DOWN)

        circle_3 = Annulus(inner_radius=0, outer_radius=0).shift(0.3*LEFT+1.1*UP)
        circle_3_ch1 = Annulus(inner_radius=0.2, outer_radius=0.4).shift(0.3*LEFT+1.1*UP)

        up_circle2 = Arc(radius=0.3,angle=-PI *2, start_angle=360*DEGREES, stroke_width=22).shift(2.6*RIGHT + UP*1)

        down_circle2 = Arc(radius=0.3,angle=PI *2, start_angle=360*DEGREES, stroke_width=22).shift(3.35*LEFT + UP*1.1)
        
        self.play(Succession(MoveToTarget(line_1h),Create(line_1h_ch1)),
                  MoveToTarget(triangle),
                  MoveToTarget(line_2v),
                  MoveToTarget(line_3v),
                  MoveToTarget(line_4h),
                  Create(line_6v),
                  Create(line_5h),
                  Create(line_upc1),
                  Create(line_dc1),
                  Uncreate(down_circle),
                  Uncreate(up_circle), 
                  run_time=1.2,
                  rate_functions= smooth)
        
        triangle.generate_target()
        triangle.target.shift(2.8*LEFT)

        self.play(MoveToTarget(line_upc1),
                  MoveToTarget(line_dc1),
                  MoveToTarget(triangle, rate_functions=slow_into,run_time=3),
                  Uncreate(line_t1, run_time=0.5),
                  Create(line_7v),
                  Create(line_8v),
                  Create(line_3_ch1),
                  FadeOut(line_3v, shift=RIGHT),
                  MoveToTarget(line_3_ch1),
                  Create(line_2v_ch1),
                  FadeOut(line_2v, shift=RIGHT),
                  Create(line_4_ch1),
                  FadeOut(line_4h,shift=UP),
                  ReplacementTransform(circle_2, circle_2_ch1),
                  run_time=1.2,
                 )
        
        line_upc2.generate_target()
        line_upc2.target.shift(1.2*DOWN).scale(0.1)
        line_dc2.generate_target()
        line_dc2.target.shift(2.2*UP).scale(0.01)

        self.play(Succession(Create(line_upc2),line_upc2.animate.stretch(0, dim=1, about_edge=DOWN), run_time=0.7),
                  Succession(Create(line_dc2),line_dc2.animate.stretch(0, dim=1, about_edge=UP),run_time=0.7),
                  FadeOut(line_upc1, shift=DOWN, run_time=0.2),
                  FadeOut(line_dc1, shift=UP, run_time=0.2),
                  Create(line_13h),
                  Create(line_14),
                  Create(line_10v),
                  Create(line_9h),
                  Create(line_11v),
                  Create(line_16v),
                  ReplacementTransform(circle_3, circle_3_ch1),
                  MoveToTarget(line_2v_ch1),
                  MoveToTarget(line_4_ch1),
                  Create(line_12h),
                  Create(up_circle2, lag_ratio=0.3),
                  Create(down_circle2, lag_ratio=0.3),
                #   triangle.animate.set_color(RED_A),
                  run_time=1.2,
                  rate_functions= slow_into)
        
        self.play(Create(line_15h),
                #   down_circle2.animate.set_color(MAROON_C),
                #   line_1h.animate.set_color(MAROON_C),
                #   line_1h_ch1.animate.set_color(MAROON_C),
                #   line_3_ch1.animate.set_color(MAROON_C),
                #   line_4_ch1.animate.set_color(MAROON_C),
                #   line_2v_ch1.animate.set_color(MAROON_C),
                #   triangle.animate.set_color(MAROON_C),
                #   run_time=1,
                #   rate_functions = lingering

        )
        self.wait(2)