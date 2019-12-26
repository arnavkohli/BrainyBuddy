from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Quiz
from .forms import QuizEditForm

from mcq.models import MCQ, MCQAnswer
from mcq.forms import MCQForm, MCQAnswerForm

from torfq.models import TorFQ
from torfq.forms import TorFQForm

from essayqu.models import EssayQ
from essayqu.forms import EssayQForm

AnswerSetForm = inlineformset_factory(parent_model=MCQ, model=MCQAnswer, fields = ('body', 'is_correct'), extra=4, max_num=4)

# Create your views here.
def QuizCreateView(request):
    if request.user.is_tutor:
        if request.method == 'GET':
            new_quiz = Quiz.objects.create(user_id=request.user.id)
            return redirect('/quiz/editQuiz/{}'.format(new_quiz.id))
    return redirect('/home/')

def save_quiz(request, quiz_id):
	quiz = Quiz.objects.get(id=quiz_id)
	form = QuizEditForm(request.POST, instance=quiz)
	if form.is_valid():
		form = form.save(commit=False)
		form.user = request.user
		form.save()
	return redirect('/home/')

def delete_quiz(request, quiz_id):
	Quiz.objects.get(id=quiz_id).delete()
	return redirect('/home/')

def save_question(request, quiz_id):
	question_body = request.POST['body']

	# mcq = MCQ.objects.create(quiz=Quiz.objects.get(id=quiz_id), body=question_body)
	mcq_form = MCQForm(request.POST)
	if mcq_form.is_valid():
		mcq = mcq_form.save(commit=False)
		mcq.quiz = Quiz.objects.get(id=quiz_id)
		mcq.save()
	answers_form = AnswerSetForm(request.POST, instance=mcq)
	if answers_form.is_valid():
		# mf = mcq_form.save(commit=False)
		# mf.quiz = Quiz.objects.get(id=quiz_id)
		# mf.save()
		answers_form.save()
	return redirect('/quiz/editQuiz/{}/'.format(quiz_id))

def save_torfq(request, quiz_id):
	torfq_form = TorFQForm(request.POST)
	if torfq_form.is_valid():
		torfq = torfq_form.save(commit=False)
		torfq.quiz = Quiz.objects.get(id=quiz_id)
		torfq.save()
	return redirect('/quiz/editQuiz/{}/'.format(quiz_id))

def save_essayq(request, quiz_id):
	essayq_form = EssayQForm(request.POST)
	if essayq_form.is_valid():
		essayq = essayq_form.save(commit=False)
		essayq.quiz = Quiz.objects.get(id=quiz_id)
		essayq.save()
	return redirect('/quiz/editQuiz/{}/'.format(quiz_id))

def remove_question(request, quiz_id):
	q_type, eyed = request.POST['removeQuestion'].split(' ')
	if q_type == 'MCQ':
		MCQ.objects.get(id=eyed).delete()
	if q_type == 'TorFQ':
		TorFQ.objects.get(id=eyed).delete()
	if q_type == 'EssayQ':
		EssayQ.objects.get(id=eyed).delete()

	return redirect('/quiz/editQuiz/{}/'.format(quiz_id))
def save_changes(request, quiz_id):
	q_type, eyed = request.POST['saveChanges'].split(' ')

	if q_type == 'MCQ':
		mcq = MCQ.objects.get(id=eyed)
		mcq_form = MCQForm(request.POST, instance=mcq)
		answers_form = AnswerSetForm(request.POST, instance=mcq)
		# answers_form.save()
		if mcq_form.save() and answers_form.is_valid():
			mcq_form.save()
			answers_form.save()

		# if mcq_form.is_valid() and answers_form.is_valid():
		# 	# mf = mcq_form.save(commit=False)
		# 	# mf.quiz = Quiz.objects.get(id=quiz_id)
		# 	mcq_form.save()
		# 	answers_form.save()
	if q_type == 'TorFQ':
		torfq = TorFQ.objects.get(id=eyed)
		torfq_form = TorFQForm(request.POST, instance=torfq)

		if torfq_form.is_valid():
			torfq_form.save()

	if q_type == 'EssayQ':
		essayq = EssayQ.objects.get(id=eyed)
		essayq_form = EssayQForm(request.POST, instance=essayq)

		if essayq_form.is_valid():
			essayq_form.save()
	return redirect('/quiz/editQuiz/{}/'.format(quiz_id))


def editing_question(request, quiz_id):
	quiz = Quiz.objects.get(id=quiz_id)
	q_type, eyed = request.POST['editQuestion'].split(' ')
	context = {}
	context['editing'] = True

	context['question_type'] = q_type
	context['question_id'] = eyed

	context['mcq'] = False
	context['torfq'] = False
	context['essayq'] = False

	if q_type == 'MCQ':
	    mcq = MCQ.objects.get(id=eyed)
	    context['quiz_form'] = QuizEditForm(instance=quiz)
	    context['question_form'] = MCQForm(instance=mcq)
	    context['answer_set_form'] = AnswerSetForm(instance=mcq)
	    context['added_questions'] = quiz.get_all_questions()
	    context['mcq'] = True
	if q_type == 'TorFQ':
		torfq = TorFQ.objects.get(id=eyed)
		context['quiz_form'] = QuizEditForm(instance=quiz)
		context['torfq_form'] = TorFQForm(instance=torfq)
		context['added_questions'] = quiz.get_all_questions()
		context['torfq'] = True
	if q_type == 'EssayQ':
		essayq = EssayQ.objects.get(id=eyed)
		context['quiz_form'] = QuizEditForm(instance=quiz)
		context['essayq_form'] = EssayQForm(instance=essayq)
		context['added_questions'] = quiz.get_all_questions()
		context['essayq'] = True

	return render(request, 'quiz/edit.html', context)

def QuizEditView(request, quiz_id):
	quiz = Quiz.objects.get(id=quiz_id)
	if request.user.is_tutor:
		context = {}
		context['quiz'] = quiz
		context['editing'] = False
		context['quiz_form'] = QuizEditForm(instance=quiz)
		context['question_form'] = MCQForm()

		context['answer_set_form'] = AnswerSetForm()
		#print (dir(context['answer_set_form'].forms[0]['is_correct']))

		context['torfq_form'] = TorFQForm()

		context['essayq_form'] = EssayQForm()

		context['added_questions'] = quiz.get_all_questions()

		if request.method == 'POST':
			if 'saveQuiz' in request.POST:
				return save_quiz(request, quiz_id)
			if 'deleteQuiz' in request.POST:
				return delete_quiz(request, quiz_id)

			if 'saveQuestion' in request.POST:
				return save_question(request, quiz_id)
			if 'saveTorFQ' in request.POST:
				return save_torfq(request, quiz_id)
			if 'saveEssayQ' in request.POST:
				return save_essayq(request, quiz_id)

			if 'removeQuestion' in request.POST:
				return remove_question(request, quiz_id)
			if 'editQuestion' in request.POST:
				return editing_question(request, quiz_id)
			if 'saveChanges' in request.POST:
				return save_changes(request, quiz_id)

	return render(request, 'quiz/edit.html', context)