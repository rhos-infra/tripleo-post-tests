# tripleo-post-tests
Infrared plugin for running post deployment verifications against a TripleO environment

Requirements
------------

The tests require an undercloud/overcloud to be available for testing the configuration against.

Contributing new tests
-----------------------------
Code changes can be submitted via [review.gerrithub.io](https://review.gerrithub.io/admin/projects/rhos-infra/tripleo-post-tests)

For adding a new test you have to to:

  - Create a new playbook including the verification tasks under the tasks/ dir:

        e.g. tasks/timesync.yml

  - Add a new option for the timesync test in plugin.spec

            - title: Validate configuration
              options:
                  timesync:
                      type: Bool
                      help: |
                          Validate undercloud and overcloud nodes time is synchronized.
                      default: False

  - Import the playbook created in the step above in the root main.yml based on the conditional option added in the previous step

            - name: Validate time is in sync
              import_playbook: tasks/timesync.yml
              when: test.timesync|default(False)

Usage with InfraRed
-----------------------------

For manual installation:

    # Install plugin
    infrared plugin add https://github.com/rhos-infra/tripleo-post-tests

    # Trigger timesync test
    infrared tripleo-config-changes --timesync yes

License
-------

Apache 2.0
