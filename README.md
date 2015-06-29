# Text-Classification

## Installing pyenv-virtualenv

1. **Install the build dependencies**

        sudo apt-get install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
        
2. **Install pyenv as regular user**

        curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

3. **Add to ~/.bashrc following code**

        export PYENV_ROOT="${HOME}/.pyenv"
        
        if [ -d "${PYENV_ROOT}" ]; then
            export PATH="${PYENV_ROOT}/bin:${PATH}"
            eval "$(pyenv init -)"
        fi

4. **Install python3**

        pyenv install 3.4.3
        
5. **Set up virtualenv**

        pyenv virtualenv text-classification-env
        
6. **Go to project directory**
        
        source activate.sh
     
        