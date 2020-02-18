from manimlib.imports import *

class Quote(Scene):
	def construct(self):
		lDQM = TextMobject("“")
		lDQM.set_color("#300a24")
		rDQM = TextMobject("”")
		rDQM.set_color(BLUE)
		quoteContent1 = TextMobject("Our industry doesn't respect tradition,")
		quoteContent2 = TextMobject("it only respects innovation.")
		emDash = TextMobject("——")
		emDash.scale(0.75)
		quoteSource = TextMobject("Satya Nadella, the CEO of Microsoft")
		quoteSource.scale(0.75)
		
		quoteContent2.next_to(quoteContent1, DOWN)
		lDQM.next_to(quoteContent1, LEFT)
		rDQM.next_to(quoteContent2, RIGHT)
		emDash.next_to(quoteContent2, DOWN)
		quoteSource.next_to(emDash, RIGHT)
		
		self.wait(1)
		self.play(Write(lDQM), Write(rDQM))
		self.wait(1)
		self.play(Write(quoteContent1))
		self.play(Write(quoteContent2))
		self.wait(1)
		self.play(Write(emDash))
		self.wait(1)
		self.play(Write(quoteSource))
		self.wait(6)