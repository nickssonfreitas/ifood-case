#!/bin/bash

# Pega UID e GID do usuário atual
USER_UID=$(id -u)
USER_GID=$(id -g)
USER_NAME=$(whoami)

# Gera ou sobrescreve o arquivo .env
cat <<EOF > .env
# Gerado automaticamente
UID=${USER_UID}
GID=${USER_GID}
USERNAME=${USER_NAME}
EOF

echo "✅ .env criado com:"
echo "   UID=${USER_UID}"
echo "   GID=${USER_GID}"
echo "   USERNAME=${USER_NAME}"