from tkinter.filedialog import askdirectory,askopenfilename
from tkinter import *
from tkinter import messagebox as msgb
from tkinter import ttk
import pygame
import random
import os





class Avatar_Music_Player:



    def __init__(self,my_music_wm):
        self.first_click=0
        self.list_of_songs=[]
        self.single_song_name=''
        self.song_index=0
        self.single_song_name=''
        self.volume=0.5
        self.my_loc=os.getcwd()
        self.check_me=-1
        self.check_pause=0
        self.check_mute=0
        self.check_stop=0
        self.gif=[]

        
        ##################################################      Main Window        ###################################################################
        self.my_music_wm=my_music_wm
        self.my_music_wm.title('Avatar Music Player')
        self.my_music_wm.resizable(0,0)
        self.my_music_wm.geometry('1200x600')
        self.my_music_wm.configure(background='black')
        self.my_music_wm.wm_iconbitmap('Avatar Icon.ico')


        #################################################         Menu Bar         ###################################################################
        self.avatar_menubar=Menu(self.my_music_wm)
        self.my_music_wm.configure(menu=self.avatar_menubar)

        
        self.media_menu=Menu(self.my_music_wm,tearoff=0)

        self.media_menu.add_command(label='Open file',command=self.browse_file)
        self.media_menu.add_command(label='Open folder',command=self.browse_folder)

        self.media_menu.add_separator()
        
        self.media_menu.add_command(label='Exit',command=self.exit_me)

        self.avatar_menubar.add_cascade(label='Media',menu=self.media_menu)


        self.playback_menu=Menu(self.my_music_wm,tearoff=0)

        self.playback_menu.add_command(label='Play Music',command=self.play_song)
        self.playback_menu.add_command(label='Stop Music',command=self.stop_song)

        self.playback_menu.add_separator()
        
        self.playback_menu.add_command(label='Next Song',command=self.next_song)
        self.playback_menu.add_command(label='Previous Song',command=self.prev_song)

        self.avatar_menubar.add_cascade(label='Playback',menu=self.playback_menu)


        self.audio_menu=Menu(self.my_music_wm,tearoff=0)

        self.audio_menu.add_command(label='Increase Volume',command=self.music_up)
        self.audio_menu.add_command(label='Decrease Volume',command=self.music_down)
        
        self.audio_menu.add_command(label='Mute',command=self.mute_song)

        self.audio_menu.add_separator()

        self.audio_menu.add_command(label='Visualizaions',command=self.change_vis)

        self.avatar_menubar.add_cascade(label='Audio',menu=self.audio_menu)


        self.help_menu=Menu(self.my_music_wm,tearoff=0)

        self.help_menu.add_command(label='About Avatar',command=self.about_dev)
        self.help_menu.add_command(label='Help Docs',command=self.help_me)
        
        self.avatar_menubar.add_cascade(label='Help',menu=self.help_menu)


        ###########################################################      Middle Logo     ##########################################################
        self.ava=PhotoImage(file='Avatar Logo.png')
        self.avatar_logo=Label(self.my_music_wm,image=self.ava,height=400,width=800,bg='black')
        self.avatar_logo.pack(padx=100,pady=20)


        ##########################################################      Song Label Bar        ##########################################################
        self.song_label_value=StringVar()
        self.song_label=Label(self.my_music_wm,textvariable=self.song_label_value,bg='black',fg='white',font=('Arial',10,'bold'))
        self.song_label.pack(fill=X,pady=5)
        self.song_label_value.set("Hiii... I'm Avatar. Here You Rock N Roll With Amazing Music Channels.")


        ##########################################################      Music Console    #########################################################
        self.play_button=Button(self.my_music_wm,text='\u25B6',width=3,font=('Arial',26,'bold'),bd=20,activebackground='grey',command=self.play_pause_song)
        self.play_button.pack(side=LEFT)

        self.prev_button=Button(self.my_music_wm,text='I\u25c0\u25c0',width=3,font=('Arial',26,'bold'),bd=20,activebackground='grey',command=self.prev_song)
        self.prev_button.pack(side=LEFT)

        self.stop_button=Button(self.my_music_wm,text='\u25A0',width=3,font=('Arial',26,'bold'),bd=20,activebackground='grey',command=self.stop_song)
        self.stop_button.pack(side=LEFT)

        self.next_button=Button(self.my_music_wm,text='\u25B6\u25B6I',width=3,font=('Arial',26,'bold'),bd=20,activebackground='grey',command=self.next_song)
        self.next_button.pack(side=LEFT)

        self.voldown_button=Button(self.my_music_wm,text='\u2B07',width=3,font=('Arial',26,'bold'),bd=20,activebackground='grey',command=self.music_down)
        self.voldown_button.pack(side=RIGHT)

        self.volup_button=Button(self.my_music_wm,text='\u2B06',width=3,font=('Arial',26,'bold'),bd=20,activebackground='grey',command=self.music_up)
        self.volup_button.pack(side=RIGHT)

        self.empty_label=Button(self.my_music_wm,height=8,width=80,text='AVATAR',font=('Colonna MT',70,'bold'),relief=FLAT,bd=0,fg='#f0f0f0',command=self.flash_avatar,activeforeground='black')
        self.empty_label.pack(side=RIGHT)



    def change_vis(self):
        os.chdir(self.my_loc)
        self.vis=os.chdir('Visualizations\\')
        for files in os.listdir(self.vis):
            if files.endswith(".gif"):
                self.gif.append(files)
        self.chgif=random.choice(self.gif)
        self.temp_gif=PhotoImage(file=self.chgif)
        self.avatar_logo.configure(image=self.temp_gif)
        if self.check_me==0:
            os.chdir(self.single_song_loc)
        else:
            os.chdir(self.folder_name)


        
    def flash_avatar(self):
        self.mycolor=['black','white','red','blue','green','yellow','pink','skyblue','purple','grey','gold','orange','darkgreen','lightgreen','darkblue','cyan','magenta','#00FF00','#FF00FF','#C0C0C0','brown','#800000','#808000','#302217','#2554C7','#25587E','#2B547E','#8D38C9','#F6358A','#800517','#7E354D','#437C17','#805817','#EDE275','#B5EAAA','#437C17']
        self.chcolor=random.choice(self.mycolor)
        self.empty_label.configure(fg=self.chcolor,activeforeground=self.chcolor)

        
    
    def music_up(self):
        if self.check_mute==1:
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.get_volume()
            self.check_mute=0
        else:
            self.volume+=0.1
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.get_volume()
            self.check_mute=0



    def music_down(self):
        if self.check_mute==1:
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.get_volume()
            self.check_mute=0
        else:
            self.volume-=0.1
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.get_volume()
            self.check_mute=0



    def next_song(self):
        if self.check_me==0:
            pass
        else:
            if self.check_stop==1 or self.check_pause==1:
                pass
            else:
                self.song_index+=1
                pygame.mixer.music.load(self.list_of_songs[self.song_index])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()
                self.update_song_label()
                self.play_button.configure(text='II')



    def prev_song(self):
        if self.check_me==0:
            pass
        else:
            if self.check_stop==1 or self.check_pause==1:
                pass
            else:
                self.song_index-=1
                pygame.mixer.music.load(self.list_of_songs[self.song_index])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()
                self.update_song_label()
                self.play_button.configure(text='II')



    def play_pause_song(self):
        if self.check_stop==1:
            if self.check_me==1:
                pygame.mixer.music.load(self.list_of_songs[self.song_index])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()
                self.play_button.configure(text='II')
                self.check_stop=0
                self.update_song_label()
            if self.check_me==0:
                pygame.mixer.music.play()
                self.play_button.configure(text='II')
                self.check_stop=0
                self.update_song_label()                
        else:
            if self.check_pause==0:
                if self.check_me==0 and self.first_click==0:
                    pass
                if self.check_me==0 and self.first_click==1:
                    pygame.mixer.music.pause()
                    self.play_button.configure(text='\u25B6')
                    self.check_pause=1
                if self.check_me==1 and self.first_click==0:
                    pass
                if self.check_me==1 and self.first_click==1:
                    pygame.mixer.music.pause()
                    self.play_button.configure(text='\u25B6')
                    self.check_pause=1
            else:
                if self.check_me==0 and self.first_click==0:
                    pass
                if self.check_me==0 and self.first_click==1:
                    pygame.mixer.music.unpause()
                    self.play_button.configure(text='II')
                    self.check_pause=0
                if self.check_me==1 and self.first_click==0:
                    pass
                if self.check_me==1 and self.first_click==1:
                    pygame.mixer.music.unpause()
                    self.play_button.configure(text='II')
                    self.check_pause=0
            
        

    def mute_song(self):
        self.check_mute=1
        pygame.mixer.music.set_volume(0.0)
        pygame.mixer.music.get_volume()
        


    def about_dev(self):
        msgb.showinfo("Adout Avatar","Version  :\t\t1.0\nDeveloped By  :\tKamal Preet Singh\nPowered By  :\tIron Boy\n\nCopyright \u00A9 2018 Avatar Pvt. Ltd.")



    def help_me(self):
        os.chdir(self.my_loc)
        self.sub_window=Toplevel(self.my_music_wm)
        self.sub_window.title('Help Docs')
        self.sub_window.wm_iconbitmap('Avatar Icon.ico')
        self.sub_window.geometry('600x400')
        self.sub_window.resizable(0,0)
        self.sub_window.lift(self.my_music_wm)
        self.sub_window.state('normal')
        self.temp_logo_pic=PhotoImage(file='Avatar Logo.png')
        self.logo_label=Label(self.sub_window,image=self.temp_logo_pic).pack()
        self.avatar_name=Label(self.sub_window,text='Avatar',font=('Colonna MT',70,'bold'),relief=FLAT,bd=0,fg='blue').pack(pady=20)
        self.step_note=Label(self.sub_window,text="1.\tSelect music file or folder from 'Media' Menu.\n2.\tThen, Click on 'Play' button to play the song.\n3.\tUse different consoles to manipulate the audio streams.\n4.\tClick on 'Exit' from 'Media' menu to quit the player.").pack(fill=X,side=LEFT)
        if self.check_me==0:
            os.chdir(self.single_song_loc)
        else:
            os.chdir(self.folder_name)


    
    def browse_file(self):
        self.first_click=1
        self.check_me=0
        single_song_name=''
        self.file_name=askopenfilename(filetypes=(('MP3 Files',"*.mp3"),("OGG Files","*.ogg"),("M4A Files","*.m4a"),('All files','*.*')))
        self.single_song_loc=os.getcwd()
        self.temp_file=self.file_name[::-1]
        for i in self.temp_file:
            if i=="/":
                break
            else:
                self.single_song_name+=i
        self.single_song_name=self.single_song_name[::-1]
        pygame.mixer.music.load(self.file_name)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        self.update_song_label()
        self.play_button.configure(text='II')



    def update_song_label(self):
        if self.check_me==0:
            self.song_label_value.set(self.single_song_name)
            return
        if self.check_me==1:
            self.song_label_value.set(self.list_of_songs[self.song_index])
            return



    def browse_folder(self):
        self.check_me=1
        self.first_click=1
        self.list_of_songs=[]
        self.folder_name=askdirectory()
        os.chdir(self.folder_name)
        for files in os.listdir(self.folder_name):
            if files.endswith(".mp3"):
                self.list_of_songs.append(files)
        pygame.mixer.music.load(self.list_of_songs[0])
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        self.update_song_label()
        self.play_button.configure(text='II')
        
            
               
    def exit_me(self):
        self.exit_confirm=msgb.askyesno("Avatar Music Player","Are you sure to exit.")
        if self.exit_confirm==True:
            self.my_music_wm.destroy()
        else:
            pass



    def play_song(self):
        if (self.check_me==0 and self.check_stop==0) or self.check_stop==1:
            pygame.mixer.music.play()
            self.update_song_label()
            self.play_button.configure(text='II')
            self.check_stop=0
        if (self.check_me==1 and self.check_stop==0) or self.check_stop==1:
            pygame.mixer.music.load(self.list_of_songs[self.song_index])
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()
            self.update_song_label()
            self.play_button.configure(text='II')
            self.check_stop=0



    def stop_song(self):
        if self.check_me==0:
            pygame.mixer.music.stop()
            self.song_label_value.set("Click on play button to listen the music.")
            self.play_button.configure(text='\u25B6')
            self.check_stop=1
        if self.check_me==1:
            pygame.mixer.music.stop()
            self.song_label_value.set("Click on play button to listen the music.")
            self.play_button.configure(text='\u25B6')
            self.check_stop=1




            
def main():
    my_music=Tk()
    pygame.mixer.init()
    Music_Player=Avatar_Music_Player(my_music)
    my_music.mainloop()




    
if __name__=="__main__":main()
