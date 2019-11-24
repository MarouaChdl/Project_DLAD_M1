#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########
#PARTIE 1 #
###########

"""

hmmer conda instal pour ddl hmmer

#chercher comment recuperer les variables que utilisateur va selectionner 
DONE=cherche une fonction qui vérifie que c'est un format fasta 
DONEdemander a utilisateur options soit pour hmmer/hmmscan les stocker dans des variables
#lancer process en Unix  cad construire commande hmmer en inserant variable python et on envoie en bash 		
DONE=renvoie le chemin du fichier que 'ltuilisateur a fait	



#import os/subprocess
https://docs.python.org/fr/2.7/library/subprocess.html#module-subprocess

os import 
comment gerer les options ? (dblout et domtblout ?)
rajouter un checkbox ?


changer les checkbox en radio

afficher un message attente quand hmmer tourne 

faire une fonction pour afficher le fichier ? 
(save le fichier ?) 


"""

#ST = sous titre
from tkinter import filedialog
from tkinter import *
import tkinter

import os


class Application:
	
	def __init__(self):
		self.fenetre=Tk()
		
		
		self.file_path=""	  #stocker le chemin du fichier que l'utilisateur a charcher
		self.file_output=""   #le nom du fichier de sortie apres le hmm
		
	#définition de le fenetre
		self.fenetre.geometry("720x480")
		self.fenetre.minsize(480,360)
		self.fenetre.title("Mon application")
		self.fenetre.config(background='#41B77F')
		
		
	#Initialisation du composant 
		self.frame=Frame(self.fenetre,bg='#41B77F')
		self.frame.pack(expand=YES)
		
	#Dictionnaire pour les checkboxs
		self.dico_checkbox = {
            'hmmerscan':IntVar(),
            'hmmersearch': IntVar()
        }
		
	#Creation des widgets pour remplir le composant
		self.cree_widget()		
		
		
	def cree_widget(self):
		#Esthetique
		self.cree_titre()
		self.cree_ST_import_file()
		
		
		#Importer fichier pour faire le hmm
		self.create_bouton_file() #Pour     
		#self.get_path_fichier()
		
		#Creation des choix soit scan soit search
		self.cree_ST_choix()
		self.cree_ST_choix_hmmersearch()
		self.cree_ST_choix_hmmerscan()
		self.cree_ST_choix_check()
		
		#remplie le dico et selectionne le type de hmm a faire 
		self.get_valeurs_checkbox()
		self.validate_check_bouton()
		
		#self.cree_ST_valeur_checkbox()
		#self.get_path_str()
		
	
######PRESENTATION			
	def cree_titre(self):
		L=Label(self.frame,text="Bienvenu sur application",font=("", 40),bg='#41B77F',fg='white')
		L.pack()
			
	def cree_ST_import_file(self):
		L=Label(self.frame,text="Importation du fichier:", font=("Courrier", 25),fg='white',bg='#41B77F')
		L.pack()
		
		
		
######CHOIX TYPEDE FICHIER	
######################################################		
	def cree_ST_choix(self):
		L=Label(self.frame,text="Veuillez choisir le type hmmer :", font=("Courrier", 25),fg='white',bg='red')
		L.pack()
		
		
	def cree_ST_choix_hmmerscan(self):
		hmmerscan=Checkbutton(self.frame,bg='#41B77F',variable=self.dico_checkbox['hmmerscan'],onvalue=1,offvalue=0,height=2,width=2)
		hmmerscan.pack(side=LEFT)
		
		L_hmmerscan=Label(self.frame,text="hmmerscan", font=("Courrier", 20),fg='white',bg='#41B77F')
		L_hmmerscan.pack(side=LEFT)
		
		#print("AAAAAAA",self.dico_checkbox['hmmerscan'])
		
		
		
	def cree_ST_choix_hmmersearch(self):
		hmmersearch=Checkbutton(self.frame,bg='#41B77F',variable=self.dico_checkbox['hmmersearch'],onvalue=1,offvalue=0,height=2,width=2)
		hmmersearch.pack(side=LEFT)
		
		L_hmmersearch=Label(self.frame,text="hmmersearch", font=("Courrier", 20),fg='white',bg='#41B77F')
		L_hmmersearch.pack(side=LEFT)
		
		#print("BBBBBBB",self.dico_checkbox['hmmersearch'])
		
	#Juste pour l'esthetique
	def cree_ST_choix_check(self):
		L=Label(self.frame,text="Vous avez choisit :", font=("Courrier", 15),fg='white',bg='red')
		L.pack(side=BOTTOM)
			
	#importante fonction 		
	def get_valeurs_checkbox(self):
		print("valeur checkbox sont :")
			
		#remplie le dicoen fonction du checkbox (sera valider via le bouton du validate_check_bouton()					
		for key,val in self.dico_checkbox.items():
			val = val.get() #ICI, je récupère les valeurs
			print('KEY:', key, 'VAL:', val)
	
			
			#Pour visualiser sur tkinter on va aussi utiliser ca pour la partie bash	
			if key =='hmmersearch' and val ==1:	
				L=Label(self.frame,text=" hmmersearch", font=("Courrier", 10),fg='white',bg='red')
				L.pack(side=BOTTOM)
				
				#gestion fichier
				#os.system('hmmsearch Pfam-A.hmm  '+self.file_path) 
				
				bashCommand='hmmsearch Pfam-A.hmm '+self.file_path+'  < '+self.file_output+'.txt'
				cp = subprocess.call(bashCommand.split(),shell=True)
				print(self.file_output)
			
		
			elif key =='hmmerscan' and val ==1:	
				L=Label(self.frame,text="hmmerscan", font=("Courrier", 10),fg='white',bg='red')
				L.pack(side=BOTTOM)
				
				os.system('hmmerscan Pfam-A.hmm  '+self.file_path)
				
				bashCommand='hmmerscan Pfam-A.hmm '+self.file_path+'  < '+self.file_output+'.txt'
				cp = subprocess.call(bashCommand.split(),shell=True)
				print(self.file_output)
			
			#~ else:
				#~ L=Label(self.frame,text="Aucun choix", font=("Courrier", 10),fg='white',bg='red')
				#~ L.pack(side=BOTTOM)
	
	def validate_check_bouton(self):	
		valide = Button(self.frame,text="Submit/run Checkbox",width=15,command=self.get_valeurs_checkbox)
		valide.pack()
		

		
		
######UPLOAD FICHIER ET KEEP LE CHEMIN	
######################################################		
	def get_path_fichier(self,event=None):
		self.filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
		self.file_path=self.filename
		print ("Le chemin du fichier de l'utilisateur est: ",self.file_path) #chemin+nom de fichier -> fopen 
		
		#~ if self.filename:
			#~ try:
				#~ print('marche')
			#~ except:
				#~ showerror("Open Source File", "Failed to read file\n'%s'" % self.filename)
				
		#return self.file_path
		
	def create_bouton_file(self):
		bouton_file=Button(self.frame, text="Importer un fichier", font=("Courrier", 25),bg='white', fg='#41B77F',
				command=self.get_path_fichier)
		bouton_file.pack(pady= 25, fill=X)
		
	

	#~ def test_subprocess(self):
		#~ cp = subprocess.run('hmmsearch Pfam-A.hmm Zobellia-galactanivorans_1000-4000.faa < Zobellia.txt', 
			#~ universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

				
	#~ def get_path_str(self):
		#~ return self.filename
				

	

My_first_app=Application()
My_first_app.fenetre.mainloop()


