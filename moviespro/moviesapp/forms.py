from django import forms

# class TeluguMovieForm(forms.Form):
#     Director_name=forms.CharField(
#         label="enter director name",
#         widget=forms.TextInput(
#               attrs={
#                    'class':'form-control',
#                    'placeholder': 'enter name'
#
#               }
#         )
#     )
#     Hero_name=forms.CharField(
#         label="enter director name",
#         widget=forms.TextInput(
#               attrs={
#                    'class': 'form-control',
#                    'placeholder': 'enter name'
#
#               }
#         )
#     )
#     Heroin_name=forms.CharField(
#         label="enter director name",
#         widget=forms.TextInput(
#               attrs={
#                    'class':'form-control',
#                    'placeholder':'enter name'
#
#               }
#         )
#     )
#     Producer_name=forms.CharField(
#         label="enter director name",
#         widget=forms.TextInput(
#               attrs={
#                    'class': 'form-control',
#                    'placeholder': 'enter producer name'
#
#               }
#         )
#     )
#     Release_dt=forms.CharField(
#         label="enter release date",
#         widget=forms.DateInput(
#               attrs={
#                    'class': 'form-control',
#                    'placeholder': 'enter date'
#
#               }
#         )
#     )
class TeluguMovieForm(forms.Form):
    Director_name = forms.CharField(max_length=50)
    Hero_name = forms.CharField(max_length=50)
    Heroin_name = forms.CharField(max_length=50)
    Producer_name = forms.CharField(max_length=50)
    Release_dt = forms.DateTimeField()