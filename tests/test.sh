#!/bin/bash

# Verifier entrypoint. Runs the pytest suite against the agent's output and
# reports results the Harbor way: a CTRF test report plus a reward written to
# /logs/verifier/reward.txt (1.0 on full pass, 0.0 otherwise).
# pytest and pytest-json-ctrf are baked into the environment image
# (environment/Dockerfile).

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
status=$?

if [ $status -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
