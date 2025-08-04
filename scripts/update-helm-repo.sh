DEPLOYMENT=$1
BRANCH="staging"
REPOSITORY_URL="https://bitbucket.org/your-repo/app-helm-chart.git"

cd .. && git clone $REPOSITORY_URL
cd app-helm-chart && git fetch
git config user.email $BB_USER
git checkout $BRANCH
sed -r -i "s/\{\{.Values.services.${DEPLOYMENT}.name\}\}:(.*)/\{\{.Values.services.${DEPLOYMENT}.name\}\}:${BITBUCKET_BUILD_NUMBER}/g" "chart/templates/${DEPLOYMENT}/deployment.yaml" || die "Updating k8s files failed"
git add -A
git commit -a -m "chore: update ${DEPLOYMENT} to ${IMAGE_NAME}"
git pull --no-rebase
git push || git pull --no-rebase || git push || die "Updating k8s files failed"


