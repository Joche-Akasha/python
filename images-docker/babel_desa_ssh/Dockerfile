FROM aka/babel_desa

RUN apt-get install -y openssh-server

#ssh
RUN useradd usu1
RUN mkdir /var/run/sshd
RUN echo 'usu1:usu1' | chpasswd

#Startup
CMD ["service ssh start"] 
EXPOSE 22 

