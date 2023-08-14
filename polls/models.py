from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Data de publicação")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Ao deletar o id de uma tabela relacionada com outra o CASCADE faz deletar os itens com o id deletado 
    choice_text = models.CharField(max_length=200)                   # da na  tabela relacionada
    votes = models.IntegerField(default=0)