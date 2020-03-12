# More than one ssh account per host #

_account 1:_  
`Mr. Putin`  
`mr.putin@yandex.ru`

_account 2:_  
`Mr. Trump`  
`mr.trump@gmail.com`

---

### ssh-key generation for Mr. Putin ###

_... do not forget to specify the file name ..._

```
> cd ~/%userprofile%/.ssh/
> ssh-keygen -t rsa -b 4096 -C "mr.putin@yandex.ru"
Generating public/private rsa key pair.
Enter file in which to save the key (~/%userprofile%/.ssh/id_rsa): id_rsa_MrPutin  # specify the file name
Enter passphrase (empty for no passphrase):  # can skip
Enter same passphrase again:  # can skip
Your identification has been saved in id_rsa_MrPutin.
Your public key has been saved in id_rsa_MrPutin.pub.
The key fingerprint is:
SHA256:nmdZJF5z1Gry/2Zfmrputin2jZX+2deQwXU33Q25aBI mr.putin@yandex.ru
The key's randomart image is:
+---[RSA 4096]----+
|              o=B|
| ...o+ooo.+..    |
|     ..+.++o     |
|  ..++o=O.       |
|        S .o.+@.o|
|      . . o o.*= |
|      o   +   .oO|
|      o     oB   |
|               o*|
+----[SHA256]-----+
```

Two files created:  
`id_rsa_MrPutin` - private key (_without extension_)  
and  
`id_rsa_MrPutin.pub` - public key

---

### ssh-key generation for Mr. Trump ###
_... do not forget to specify the file name ..._

```
> cd ~/%userprofile%/.ssh/
> ssh-keygen -t rsa -b 4096 -C "mr.trump@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (~/%userprofile%/.ssh/id_rsa): id_rsa_MrTrump  # specify the file name
Enter passphrase (empty for no passphrase):  # can skip
Enter same passphrase again:  # can skip
Your identification has been saved in id_rsa_MrTrump.
Your public key has been saved in id_rsa_MrTrump.pub.
The key fingerprint is:
SHA256:EssBed6AYMP/afjmrtrumpgvkvVFRwTjXHm/Q0bAA18 mr.trump@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
| .+..ooo++..E    |
|          E  o..X|
|   . o=+ ..+     |
|    ..o+o   +    |
|     ++oS     o .|
|  . . =.o        |
| o.. *       .   |
|  +oo   .o =     |
|o oo  +o+   ..+o |
+----[SHA256]-----+
```

Two files created:  
`id_rsa_MrTrump` - private key (_without extension_)  
and  
`id_rsa_MrTrump.pub` - public key

---

### Config file ###

Create a file `~/%userprofile%/.ssh/config` :

```
# Github for "Mr. Putin"
Host mrputin.github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_MrPutin

# Github for "Mr. Trump"
Host mrtrump.github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_MrTrump
```

---

### Connection

**Connection for `Mr. Putin`**  
`git@github.com:MrPutin/foreign_policy.git`  
_change to:_  
`git@mrputin.github.com:MrPutin/foreign_policy.git`

**Connection for `Mr. Trump`**  
`git@github.com:MrTrump/domestic_policy.git`  
_change to:_  
`git@mrtrump.github.com:MrTrump/domestic_policy.git`
