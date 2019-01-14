---
config:
    plugin_type: test
subparsers:
    tripleo-post-tests:
        description: TripleO post deployment tester
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Validate configuration
              options:
                  timesync:
                      type: Bool
                      help: |
                          Validate undercloud and overcloud nodes time is synchronized.
                      default: False

            - title: Overcloud Options
              options:
                  overcloud-stack:
                      type: Value
                      help: Overrides the overcloud stack name
                      default: "overcloud"
