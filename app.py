def main():

st.title("BugBuster: Automated Code Debugging Tool")

st.markdown("""

<h2>Project Description</h2>

<p>BugBuster: AI-Powered Code Debugger" is an advanced tool designed to streamline the process of identifying and resolving errors in code. 

""", unsafe_allow_html=True)

st.markdown("""

<h2>Scenario 1: Debugging Complex Algorithms</h2>

<p>In scenarios where developers are working on complex algorithms or data structures, BugBuster can be invaluable. It helps identify logical errors,boundary condition issues, and performance bottlenecks, ensuring the algorithm functions as intended and delivers optimal results """, unsafe_allow_html=True)

st.markdown("""

<h2>Scenario 2: Code Reviews and Quality Assurance</h2>

<p>BugBuster can be integrated into code review processes and quality assurance workflows within corporate environments. It assists code reviewers in identifying potential bugs, improving code readability, and ensuring adherence to coding standards. Quality assurance teams can use BugBuster to conduct comprehensive testing and validate the functionality of software applications before deployment, reducing the risk of post-release issues.

""", unsafe_allow_html=True)

st.markdown("""

<h2>Scenario 3: Cross-Platform Compatibility</h2>

<p>BugBuster can play a vital role in ensuring consistent functionality and performance across platforms where a software product needs to be compatible across multiple platforms, such as Windows, macOS, and Linux by debugging and optimizing the codebase for each environment. Developers can use BugBuster to identify platform-specific bugs, optimize code for resource efficiency, and implement platform-specific features or optimizations. This ensures a seamless user experience across diverse platforms, enhancing the product's market reach and user satisfaction. """, unsafe_allow_html=True)

st.markdown("""

<h2>Scenario 4: Compliance and Security Audits</h2>

<p>In regulated industries such as finance, healthcare, or government, corporations must adhere to strict compliance and security standards to protect sensitive data and ensure regulatory compliance. BugBuster can assist in this context by identifying security vulnerabilities, compliance violations, and potential data breaches within the codebase. Developers and security experts can leverage BugBuster to perform automated code audits, detect security flaws, and implement necessary fixes or mitigations to ensure compliance with industry regulations and safeguard corporate assets and sensitive information

""", unsafe_allow_html=True)


st.subheader("Code Debugging")
code_snippet = st.text_area("Enter the code snippet you want to debug:")
if st.button("Debug Code"):
     if code_snippet.strip():
         with st.spinner("Debugging code..."):
             try:
                  debug_result = debug_code(code_snippet)
                  st.success("Debugging complete!")
                  st.text_area("Debugging result:", debug_result, height=300) 
             except Exception as e:
                  st.error(f"Error debugging code: {e}")
    else:
        st.error("Please enter a code snippet.")
if name "_main_":
    main()
