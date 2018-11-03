## Generate SSH Keys
```ssh-keygen``` and enter the passphrase \
go to ```~/.ssh/``` and rename **id_rsa.pub** to **authorized_keys** \
Transfer ```id_rsa``` to your host \
Connect via SSH using private key by ```ssh user@host -i path/to/key```

## Disable Password authentication
In *line 57* in ```/etc/ssh/sshd_config``` change ```PasswordAuthentication``` to no.

Proof: https://asciinema.org/a/zUGLbYNQ11nugfg4RCC83aRmh