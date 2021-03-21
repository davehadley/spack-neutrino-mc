pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                echo 'Install'
                sh '''#!/usr/bin/env bash
                    ./install.sh && source setup.sh
                    echo "--- Environment variables"
                    env
                    echo "--- Working Directory"
                    pwd
                    echo "--- Directory Contents"
                    ls 
                    '''
                
            }
        }
        stage('GENIE') { 
            stages {
                stage('Build GENIE') {
                    steps {
                        echo 'Build ROOT Extensions'
                        sh '''#!/usr/bin/env bash
                        source setup.sh
                        for GENIE_VERSION in $(echo 3.0.6 2.12.10 2.10.10 2.8.6); do
                            spack install genie@${GENIE_VERSION}+test+vleextension+validationtools+t2k+fnal+atmo+nucleondecay+masterclass;
                            if [ $? -eq 0 ]; then
                                echo ${GENIE_VERSION} OK!;
                            else
                                ERRCODE=$?
                                echo ${GENIE_VERSION} FAILED with ${ERRCODE}!;
                                exit ${ERRCODE};
                            fi;
                        done;
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Build completed'
        }
        success {
            echo 'Build was successful'
            cleanWs()
        }
        failure {
            echo 'Build failed'
        }
        unstable {
            echo 'Build unstable'
        }
        changed {
            echo 'Build status changed'
        }
    }
}