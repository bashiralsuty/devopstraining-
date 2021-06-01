from odoo import models,fields, api
from odoo.exceptions import UserError
class Student(models.Model):
	_name = "school.student"
	name = fields.Char(string="Student's Name", required=True)
	number = fields.Integer()
	description = fields.Text()
	birth_date = fields.Date()
	image = fields.Binary()
	cv = fields.Html(help="Enter the student CV")
	gender = fields.Selection(selection=[("male","Male"),("female","Female")], default="male")
	is_register = fields.Boolean()
	year = fields.Datetime()
	salary = fields.Float()
	age = fields.Integer()
	state = fields.Selection(selection=[('draft', 'Draft'), 
		('accept', 'Accept'), ('reject', 'Reject'),
	 ('graduate', 'Graduate')], default='draft')
	subjects = fields.Many2many("school.subject")
	class_id = fields.Many2one("school.class.room")
	@api.model
	def create(self, vals):
		if 'age' in vals and vals['age'] < 5:
			raise UserError('Age Must be more than or equal 5')
		new_record = super(Student, self).create(vals)
		return new_record

	def write(self, vals):
		if 'age' in vals and vals['age'] < 5:
			raise UserError('Heeeeeey Age Must be more than or equal 5')
		return super(Student, self).write(vals)

	def accept(self):
		self.state ='accept'
	def reject(self):
		self.state = 'reject'
	def graduate(self):
		self.state = 'graduate'

class Lesson(models.Model):
	_name = "school.lesson"
	name = fields.Char()
	number = fields.Integer()
	content = fields.Text()
class Subject(models.Model):
	_name = "school.subject"
	name = fields.Char()
	description = fields.Text()
	
class Teacher(models.Model):
	_name = "school.teacher"
	_inherit = "hr.employee"

	rooms_ids = fields.Many2many("school.class.room")
	category_ids = fields.Char()

class ClassRoom(models.Model):
	_name = "school.class.room"
	name = fields.Char()
	students = fields.One2many("school.student","class_id")

class Employee(models.Model):
	_inherit = "hr.employee"

	hiring_date = fields.Date(required=True)
	job_degree = fields.Selection([
		('1','First'),
		('2','Second'),
		('3','Third'),
		('4','Forth'),
		('5','Fifth'),
		('6','Sixth'),
		('7','Seventh'),
		('8','Eighth'),
		('9','Nineth'),
	],default="9")