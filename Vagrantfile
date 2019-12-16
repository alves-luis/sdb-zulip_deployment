Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 1
  end

  N = 5
  (1..N).each do |machine_id|
    config.vm.define "machine#{machine_id}" do |machine|
      machine.vm.hostname = "machine#{machine_id}"
      machine.vm.network "private_network", ip: "192.168.77.#{20+machine_id}"

      if machine_id != N
        machine.vm.provider :virtualbox do |vb|
          vb.memory = 512
          vb.cpus = 1
        end
      end

      # Only execute once the Ansible provisioner,
      # when all the machines are up and ready.
      if machine_id == N
        machine.vm.provider :virtualbox do |vb|
          vb.memory = 4000
          vb.cpus = 1
        end
        machine.vm.provision :ansible do |ansible|
          # Disable default limit to connect to all the machines
          ansible.raw_arguments = [
            "-e ansible_python_interpreter=/usr/bin/python3"
          ]
          ansible.limit = "all"
          ansible.groups = {
            "postgres" => ["machine1"],
            "memcached" => ["machine2"],
            "redis" => ["machine3"],
            "rabbitmq" => ["machine4"],
            "zulip" => ["machine5"],
          }
          ansible.playbook = "playbook.yml"
        end
      end
    end
  end

end
