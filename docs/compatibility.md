# 🧩 Compatibility

## Runtime dependencies
The project declares Flask, NumPy, pandas, and Gunicorn in `requirements.txt`. Versions are not pinned. The notebook imports scikit-learn, which is not currently listed in the runtime requirements file.

## Python and operating systems
The repository does not declare a tested Python version matrix. Use a maintained Python 3 release and verify dependency installation and pickle compatibility in the target environment. Test on the actual deployment OS before release.

## Artifact compatibility
Pickle compatibility depends on Python and library versions as well as object structure. Keep the build environment recorded and test loading artifacts in the exact deployment image.

## Browser compatibility
The templates use standard HTML and CSS. No formal browser support matrix or automated cross-browser tests are present. Verify current Chrome, Firefox, Safari, and mobile browser behavior before claiming support.
