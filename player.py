import pygame

import config as c

from game_object import GameObject

class Player(GameObject):

	R_SQRT = 0.7071067811865475

	def __init__(self, x, y, w, h, color, offset):
		GameObject.__init__(self, x, y, w, h)
		self.color = color
		self.offset = offset
		self.actions = {'moving_left': False,
		 				'moving_right': False,
		  				'moving_up': False,
		   				'moving_down': False}

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.bounds)

	def handle(self, key):
		key_action_dict = {
			pygame.K_LEFT: 'moving_left',
			pygame.K_RIGHT: 'moving_right',
			pygame.K_UP: 'moving_up',
			pygame.K_DOWN: 'moving_down'
		}
		action = key_action_dict[key];
		self.actions[action] = not self.actions[action]

	def update(self):
		#add dx offset to real, dy offset to imag
		dx_dy_offset = {
			'moving_left': complex(-(min(self.offset, self.left)), 0),
			'moving_right': complex(min(self.offset, c.screen_width - self.right), 0),
			'moving_up': complex(0, -(min(self.offset, self.top))),
			'moving_down': complex(0, min(self.offset, c.screen_height - self.bottom))
		}
		dxdy = 0 + 0j

		for move, status in self.actions.items():
			if status:	
				dxdy += dx_dy_offset[move]

		if dxdy.real > 0 and dxdy.imag > 0:
			self.move(dxdy.real * self.R_SQRT, dxdy.imag * self.R_SQRT)
		else:
			self.move(dxdy.real, dxdy.imag)
