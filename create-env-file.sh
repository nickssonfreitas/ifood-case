#!/bin/bash

# Pega UID e GID do usuário atual
USER_UID=$(id -u)
USER_GID=$(id -g)

# Gera ou sobrescreve o arquivo .env
cat <<EOF > .env
# Gerado automaticamente
UID=${USER_UID}
GID=${USER_GID}
EOF

echo "✅ .env criado com UID=${USER_UID} e GID=${USER_GID}"
