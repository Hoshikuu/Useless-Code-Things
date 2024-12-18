#!/bin/bash
# Script per a la configuració del servidor Linux segons els requeriments

# 1. Creació de grups d'usuaris
# -----------------------------
groupadd esobat
groupadd smx
groupadd asidai
groupadd profeeso
groupadd profeinf
groupadd vigilant

groupadd alumnes
groupadd professors

# 2. Creació d'usuaris i assignació als grups
# -----------------------------
# Exemple de creació d'usuari per a cada grup (afegiràs tants usuaris com necessaris)
useradd -m -g esobat -G alumnes,vigilant alumneESO1
useradd -m -g smx -G alumnes,vigilant alumneSMX1
useradd -m -g asidai -G alumnes,vigilant alumneASIDAI1
useradd -m -g profeeso -G professors professorESO1
useradd -m -g profeinf -G professors professorINF1
useradd -m -g vigilant vigilant1

# 3. Configuració de permisos per a les carpetes individuals
# -----------------------------
for user in $(getent group esobat | cut -d: -f4 | tr ',' ' '); do
    chmod 700 /home/$user
    usermod -aG alumnes,vigilant $user
done

for user in $(getent group smx | cut -d: -f4 | tr ',' ' '); do
    chmod 700 /home/$user
    usermod -aG alumnes,vigilant $user
done

for user in $(getent group asidai | cut -d: -f4 | tr ',' ' '); do
    chmod 700 /home/$user
    usermod -aG alumnes,vigilant $user
done

for user in $(getent group profeeso | cut -d: -f4 | tr ',' ' '); do
    chmod 700 /home/$user
    usermod -aG professors $user
done

for user in $(getent group profeinf | cut -d: -f4 | tr ',' ' '); do
    chmod 700 /home/$user
    usermod -aG professors $user
done

for user in $(getent group vigilant | cut -d: -f4 | tr ',' ' '); do
    chmod 700 /home/$user
done

# 4. Creació de les carpetes generals a /home
# -----------------------------
mkdir /home/alumnes
mkdir /home/professors
mkdir /home/informatica

# Assignació de propietari i permisos
chown root:alumnes /home/alumnes
chmod 770 /home/alumnes

chown root:professors /home/professors
chmod 770 /home/professors

chown root:professors /home/informatica
chmod 770 /home/informatica

# Configuració de permisos per a les carpetes generals
chmod 770 /home/alumnes
chmod 770 /home/professors
chmod 770 /home/informatica

# 5. Creació i configuració de fitxers dins la carpeta informatica
# -----------------------------
touch /home/informatica/GSuperior.txt
chown root:asidai /home/informatica/GSuperior.txt
chmod 664 /home/informatica/GSuperior.txt


touch /home/informatica/ProfeInformatica.txt
chown root:profeinf /home/informatica/ProfeInformatica.txt
chmod 660 /home/informatica/ProfeInformatica.txt

# 6. Resum de permisos
# -----------------------------
# /home/alumnes: 
#   - alumnes poden llegir i escriure (esobat, smx, asidai)
#   - professors no poden accedir
#   - vigilant té accés total
#
# /home/professors: 
#   - només professors (profeeso, profeinf) tenen accés complet
#   - alumnes i vigilant no poden accedir
#
# /home/informatica: 
#   - alumnes (smx, asidai) poden llegir
#   - professors d'informàtica (profeinf) tenen accés complet
#   - altres usuaris no poden accedir
#
# Fitxer GSuperior.txt:
#   - alumnes de grau superior (asidai) poden llegir i escriure
#   - alumnes de grau mitjà (smx) i professors d'informàtica (profeinf) només poden llegir
#
# Fitxer ProfeInformatica.txt:
#   - professors d'informàtica (profeinf) tenen control total
#   - la resta d'usuaris no poden ni llegir el fitxer
