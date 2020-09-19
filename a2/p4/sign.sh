#!/bin/bash
# source: zeali.net
 
#length of the key
lengthbit=4096
#the dirctory of the certificate
sslOutputRoot="."
if [ $# -eq 1 ]; then
	sslOutputRoot=$1
fi
if [ ! -d ${sslOutputRoot} ]; then
	mkdir -p ${sslOutputRoot}
fi
 
cd ${sslOutputRoot}
 
echo "start creating the licence..."
#start creating the CA root certificate
# generate the private key for root CA 
 
openssl genrsa -des3 -out ca.key $lengthbit
 
[ $? != 0 ] && echo failed to generate the private key && exit 1
 
echo  "generate the root CA certificate"
 
openssl req -new -x509 -days 365 -key ca.key -out ca.crt
 
[ $? != 0 ] && echo failed to create the root CA certificate && exit 1
echo "root CA certificat done"
 
ech"start generate server key"
 
openssl genrsa -des3 -out server.key $lengthbit
#signing using the server key
 
openssl req -new -key server.key -out server.csr
 
[ $? != 0 ] && echo fail the sign and generate the server key && exit 2
ls -altrh  ${sslOutputRoot}/server.*
echo "sign and gernerate the server key done"
 
echo "sign a SSL Certificate Request(CSR)"
# 参见 http://www.faqs.org/docs/securing/chap24sec195.html
 
CSR=server.csr
 
case $CSR in
*.csr ) CERT="`echo $CSR | sed -e 's/\.csr/.crt/'`" ;;
* ) CERT="$CSR.crt" ;;
esac
 
#   make sure environment exists
if [ ! -d ca.db.certs ]; then
	mkdir ca.db.certs
fi
if [ ! -f ca.db.serial ]; then
	echo '01' >ca.db.serial
fi
if [ ! -f ca.db.index ]; then
	cp /dev/null ca.db.index
fi
 
#   create an own SSLeay config
# make it verify 10 years length
cat >ca.config <<EOT
[ ca ]
default_ca	= CA_own
[ CA_own ]
dir	= .
certs	= .
new_certs_dir	= ./ca.db.certs
database	= ./ca.db.index
serial	= ./ca.db.serial
RANDFILE	= ./ca.db.rand
certificate	= ./ca.crt
private_key	= ./ca.key
default_days	= 3650
default_crl_days	= 30
default_md	= md5
preserve	= no
policy	= policy_anything
[ policy_anything ]
countryName	= optional
stateOrProvinceName	= optional
localityName	= optional
organizationName	= optional
organizationalUnitName	= optional
commonName	= supplied
emailAddress	= optional
EOT
 
#  sign the certificate
echo "CA sign: $CSR -> $CERT:"
openssl ca -config ca.config -out $CERT -infiles $CSR
echo "CA authentication: $CERT <-> CA cert"
openssl verify -CAfile ./ca.crt $CERT
 
[ $? != 0 ] && echo CA authentication fail && exit 3
 
#  cleanup after SSLeay
rm -f ca.config
rm -f ca.db.serial.old
rm -f ca.db.index.old
#  sign.sh END
echo "SSL sign done"
 
# make sure the key cannot be modifed by others
chmod 400 server.keyr
 
#  die gracefully
exit 0
