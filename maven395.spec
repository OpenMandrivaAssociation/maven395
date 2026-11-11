Name:		maven395
Version:	3.9.5
Release:	1
Summary:	Apache Maven 3.9.5 libraries
Group:		Development/Java
License:	Apache-2.0
URL:		https://maven.apache.org/ref/3.9.5/
# Apache Maven 3.9.5 source, main sources of the library modules only.
# Test fixtures ship prebuilt jars and are not part of this archive.
# The unversioned Maven 3.10.0 jars stay in maven-components.
Source0:	maven-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	java-current-devel
BuildRequires:	sysjar
BuildRequires:	modello
BuildRequires:	mvn(org.codehaus.plexus:plexus-utils) = 3.6.2
BuildRequires:	mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:	mvn(org.codehaus.plexus:plexus-interpolation) = 1.26
BuildRequires:	mvn(org.codehaus.plexus:plexus-classworlds) = 2.7.0
BuildRequires:	mvn(org.codehaus.plexus:plexus-component-annotations) = 2.2.0
BuildRequires:	mvn(org.codehaus.plexus:plexus-sec-dispatcher) = 2.0
BuildRequires:	mvn(org.codehaus.plexus:plexus-cipher) = 2.0
BuildRequires:	mvn(org.apache.commons:commons-lang3) = 3.21.0
BuildRequires:	mvn(javax.inject:javax.inject) = 1.0.5
BuildRequires:	mvn(org.eclipse.sisu:org.eclipse.sisu.inject) = 0.3.5
BuildRequires:	mvn(org.eclipse.sisu:org.eclipse.sisu.plexus) = 0.3.5
BuildRequires:	mvn(com.google.inject:guice) = 5.1.0
BuildRequires:	mvn(com.google.guava:guava) = 33.6.0-jre
BuildRequires:	mvn(com.google.guava:failureaccess) = 1.0.3
BuildRequires:	mvn(aopalliance:aopalliance)
BuildRequires:	mvn(org.slf4j:slf4j-api) = 2.0.17
BuildRequires:	mvn(org.apache.maven.wagon:wagon-provider-api) = 3.5.3
BuildRequires:	mvn(org.apache.maven.shared:maven-shared-utils) = 3.5.0
BuildRequires:	mvn(org.apache.maven.resolver:maven-resolver-api) = 1.9.16
BuildRequires:	mvn(org.apache.maven.resolver:maven-resolver-spi) = 1.9.16
BuildRequires:	mvn(org.apache.maven.resolver:maven-resolver-util) = 1.9.16
BuildRequires:	mvn(org.apache.maven.resolver:maven-resolver-named-locks) = 1.9.16
BuildRequires:	mvn(org.apache.maven.resolver:maven-resolver-impl) = 1.9.16

Requires:	mvn(org.codehaus.plexus:plexus-utils) = 3.6.2
Requires:	mvn(org.codehaus.plexus:plexus-interpolation) = 1.26
Requires:	mvn(org.codehaus.plexus:plexus-classworlds) = 2.7.0
Requires:	mvn(org.codehaus.plexus:plexus-component-annotations) = 2.2.0
Requires:	mvn(org.codehaus.plexus:plexus-sec-dispatcher) = 2.0
Requires:	mvn(org.apache.commons:commons-lang3) = 3.21.0
Requires:	mvn(javax.inject:javax.inject) = 1.0.5
Requires:	mvn(org.eclipse.sisu:org.eclipse.sisu.inject) = 0.3.5
Requires:	mvn(org.eclipse.sisu:org.eclipse.sisu.plexus) = 0.3.5
Requires:	mvn(com.google.inject:guice) = 5.1.0
Requires:	mvn(com.google.guava:guava) = 33.6.0-jre
Requires:	mvn(com.google.guava:failureaccess) = 1.0.3
Requires:	mvn(org.slf4j:slf4j-api) = 2.0.17
Requires:	mvn(org.apache.maven.wagon:wagon-provider-api) = 3.5.3
Requires:	mvn(org.apache.maven.shared:maven-shared-utils) = 3.5.0
Requires:	mvn(org.apache.maven.resolver:maven-resolver-api) = 1.9.16
Requires:	mvn(org.apache.maven.resolver:maven-resolver-spi) = 1.9.16
Requires:	mvn(org.apache.maven.resolver:maven-resolver-util) = 1.9.16
Requires:	mvn(org.apache.maven.resolver:maven-resolver-impl) = 1.9.16
Requires:	mvn(org.apache.maven.resolver:maven-resolver-named-locks) = 1.9.16

%description
Apache Maven %{version} model, artifact, settings, plugin API, core,
compat, and the resolver provider. Gradle 9.9.1 pins these coordinates
exactly, so the Maven 3.10.0 jars in maven-components do not satisfy
them. Jars and sysjar indexes are versioned and do not replace the
unversioned 3.10.0 indexes. Modello generates the readers and writers.
The extended model writer that emits a null class name is not compiled.

%prep
%autosetup -n maven-%{version}
find . \( -name '*.jar' -o -name '*.class' -o -name '*.so' -o -name '*.node' -o -name '*.wasm' \) -delete

%build
set -eo pipefail
export JAVA_HOME=%{_jvmdir}/java-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
J=%{_javadir}
PU=$J/plexus-utils.jar
PX=$J/plexus-xml.jar
LANG=$J/commons-lang3.jar
PI=$J/plexus-interpolation-1.26.jar
INJ=$J/atinject.jar
SISU=$J/org.eclipse.sisu.inject-0.3.5.jar
SISP=$J/org.eclipse.sisu.plexus-0.3.5.jar
SEC=$J/plexus/plexus-sec-dispatcher.jar
CIPHER=$J/plexus-cipher.jar
CW=$J/plexus-classworlds-2.7.0.jar
WAGON=$J/maven-wagon/provider-api.jar
SLF=$J/slf4j-api.jar
GUICE=$J/google-guice.jar
GUAVA=$J/guava.jar
FA=$J/failureaccess.jar
AOP=$J/aopalliance.jar
ANN=$J/plexus-containers/plexus-component-annotations.jar
SHARED=$J/maven-shared-utils.jar
API=$J/maven-resolver-api-1.9.16.jar
SPI=$J/maven-resolver-spi-1.9.16.jar
UTIL=$J/maven-resolver-util-1.9.16.jar
LOCKS=$J/maven-resolver-named-locks-1.9.16.jar
IMPL=$J/maven-resolver-impl-1.9.16.jar
RES="$API:$SPI:$UTIL:$IMPL:$LOCKS"
RUNCP="$J/modello-core.jar:$J/modello-plugin-java.jar:$J/modello-plugin-xml.jar:$J/modello-plugin-xpp3.jar"
RUNCP="$RUNCP:$PX:$PU:$J/plexus-build-api.jar:$SISP:$SISU:$GUICE:$GUAVA:$FA:$INJ:$AOP"
RUNCP="$RUNCP:$CW:$ANN:$SLF"

gen() {
	module="$1"
	mdo="$2"
	ver="$3"
	shift 3
	out="$module/target/generated-sources"
	mkdir -p "$out"
	for goal in "$@"; do
		java -cp "$RUNCP" org.codehaus.modello.ModelloCli "$module/src/main/mdo/$mdo" "$goal" "$out" "$ver" false 8 UTF-8
	done
}

gen maven-model maven.mdo 4.0.0 java xpp3-reader xpp3-writer xpp3-extended-reader xpp3-extended-writer
gen maven-settings settings.mdo 1.2.0 java xpp3-reader xpp3-writer
gen maven-repository-metadata metadata.mdo 1.1.0 java xpp3-reader xpp3-writer
gen maven-plugin-api lifecycle.mdo 1.0.0 java xpp3-reader xpp3-writer
gen maven-core toolchains.mdo 1.1.0 java xpp3-reader xpp3-writer
gen maven-compat profiles.mdo 1.0.0 java xpp3-reader xpp3-writer
gen maven-compat paramdoc.mdo 1.0.0 java xpp3-reader xpp3-writer

compile() {
	module="$1"
	expect="$2"
	cp="$3"
	: > "$module.sources"
	if [ -d "$module/src/main/java" ]; then
		find "$module/src/main/java" -name '*.java' ! -name 'module-info.java' >> "$module.sources"
	fi
	if [ -d "$module/target/generated-sources" ]; then
		find "$module/target/generated-sources" -name '*.java' ! -name '*null.java' ! -name 'module-info.java' >> "$module.sources"
	fi
	test "$(wc -l < "$module.sources")" -eq "$expect"
	rm -rf "$module/classes"
	mkdir -p "$module/classes"
	javac --release 8 -encoding UTF-8 -Xlint:-options -proc:none -cp "$cp" -d "$module/classes" @"$module.sources"
	if [ -d "$module/src/main/resources" ]; then
		cp -a "$module/src/main/resources/." "$module/classes/"
		find "$module/classes" -type f \( -name '*.properties' -o -name '*.xml' -o -name '*.txt' \) -exec sed -i \
			-e 's/%%{project.version}/%{version}/g' \
			-e 's/%%{buildNumber}/1/g' \
			-e 's/%%{distributionId}/apache-maven/g' \
			-e 's/%%{distributionShortName}/Maven/g' \
			-e 's/%%{distributionName}/Apache Maven/g' \
			{} +
	fi
	jar cf "$module.jar" -C "$module/classes" .
	jar i "$module.jar"
	jar tf "$module.jar" | grep -E '\.(java|jar|so|node|wasm)$' && exit 1 || true
}

compile maven-builder-support 9 ""
compile maven-artifact 27 "$PU:$PX:$LANG"
compile maven-model 53 "$PU:$PX"
compile maven-repository-metadata 7 "$PU:$PX"
compile maven-settings 17 "$PU:$PX"
compile maven-plugin-api 25 "maven-model.jar:maven-artifact.jar:$PU:$PX:$SISP:$SISU:$CW:$INJ:$GUAVA:$FA:$AOP:$GUICE"
compile maven-model-builder 96 "maven-model.jar:maven-artifact.jar:maven-builder-support.jar:$PU:$PX:$PI:$INJ:$SISU:$SLF"
compile maven-settings-builder 30 "maven-settings.jar:maven-builder-support.jar:$PU:$PX:$PI:$INJ:$SEC:$CIPHER:$SLF"
compile maven-resolver-provider 27 "maven-model.jar:maven-model-builder.jar:maven-artifact.jar:maven-builder-support.jar:maven-repository-metadata.jar:$RES:$PU:$PX:$INJ:$GUICE:$GUAVA:$FA:$AOP:$SISU:$SLF"
CORECP="maven-model.jar:maven-settings.jar:maven-settings-builder.jar:maven-builder-support.jar:maven-repository-metadata.jar:maven-artifact.jar:maven-plugin-api.jar:maven-model-builder.jar:maven-resolver-provider.jar:$RES:$SHARED:$SISP:$SISU:$GUICE:$GUAVA:$FA:$AOP:$INJ:$PU:$PX:$CW:$PI:$ANN:$LANG:$SLF:$WAGON"
compile maven-core 363 "$CORECP"
compile maven-compat 146 "$CORECP:maven-core.jar"
javap -verbose -cp maven-model.jar org.apache.maven.model.Model | grep -F -q 'major version: 52'

write_pom() {
	art="$1"
	shift
	cat > "$art.pom" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.apache.maven</groupId>
  <artifactId>$art</artifactId>
  <version>%{version}</version>
  <name>$art</name>
  <description>Apache Maven %{version}.</description>
  <licenses>
    <license>
      <name>Apache-2.0</name>
    </license>
  </licenses>
  <dependencies>
EOF
	for dep in "$@"; do
		IFS=: read -r g a v << EOF2
$dep
EOF2
		cat >> "$art.pom" << EOF
    <dependency>
      <groupId>$g</groupId>
      <artifactId>$a</artifactId>
      <version>$v</version>
    </dependency>
EOF
	done
	printf '%s\n' '  </dependencies>' '</project>' >> "$art.pom"
}

write_pom maven-builder-support
write_pom maven-artifact \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	org.apache.commons:commons-lang3:3.21.0
write_pom maven-model \
	org.codehaus.plexus:plexus-utils:3.6.2
write_pom maven-repository-metadata \
	org.codehaus.plexus:plexus-utils:3.6.2
write_pom maven-settings \
	org.codehaus.plexus:plexus-utils:3.6.2
write_pom maven-plugin-api \
	org.apache.maven:maven-model:%{version} \
	org.apache.maven:maven-artifact:%{version} \
	org.eclipse.sisu:org.eclipse.sisu.plexus:0.3.5 \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	org.codehaus.plexus:plexus-classworlds:2.7.0
write_pom maven-model-builder \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	org.codehaus.plexus:plexus-interpolation:1.26 \
	javax.inject:javax.inject:1.0.5 \
	org.apache.maven:maven-model:%{version} \
	org.apache.maven:maven-artifact:%{version} \
	org.apache.maven:maven-builder-support:%{version} \
	org.eclipse.sisu:org.eclipse.sisu.inject:0.3.5
write_pom maven-settings-builder \
	org.apache.maven:maven-builder-support:%{version} \
	javax.inject:javax.inject:1.0.5 \
	org.codehaus.plexus:plexus-interpolation:1.26 \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	org.apache.maven:maven-settings:%{version} \
	org.codehaus.plexus:plexus-sec-dispatcher:2.0
write_pom maven-resolver-provider \
	org.apache.maven:maven-model:%{version} \
	org.apache.maven:maven-model-builder:%{version} \
	org.apache.maven:maven-repository-metadata:%{version} \
	org.apache.maven.resolver:maven-resolver-api:1.9.16 \
	org.apache.maven.resolver:maven-resolver-spi:1.9.16 \
	org.apache.maven.resolver:maven-resolver-util:1.9.16 \
	org.apache.maven.resolver:maven-resolver-impl:1.9.16 \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	javax.inject:javax.inject:1.0.5
write_pom maven-core \
	org.apache.maven:maven-model:%{version} \
	org.apache.maven:maven-settings:%{version} \
	org.apache.maven:maven-settings-builder:%{version} \
	org.apache.maven:maven-builder-support:%{version} \
	org.apache.maven:maven-repository-metadata:%{version} \
	org.apache.maven:maven-artifact:%{version} \
	org.apache.maven:maven-plugin-api:%{version} \
	org.apache.maven:maven-model-builder:%{version} \
	org.apache.maven:maven-resolver-provider:%{version} \
	org.apache.maven.resolver:maven-resolver-impl:1.9.16 \
	org.apache.maven.resolver:maven-resolver-api:1.9.16 \
	org.apache.maven.resolver:maven-resolver-spi:1.9.16 \
	org.apache.maven.resolver:maven-resolver-util:1.9.16 \
	org.apache.maven.shared:maven-shared-utils:3.5.0 \
	org.eclipse.sisu:org.eclipse.sisu.plexus:0.3.5 \
	org.eclipse.sisu:org.eclipse.sisu.inject:0.3.5 \
	com.google.inject:guice:5.1.0 \
	com.google.guava:guava:33.6.0-jre \
	com.google.guava:failureaccess:1.0.3 \
	javax.inject:javax.inject:1.0.5 \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	org.codehaus.plexus:plexus-classworlds:2.7.0 \
	org.codehaus.plexus:plexus-interpolation:1.26 \
	org.codehaus.plexus:plexus-component-annotations:2.2.0 \
	org.apache.commons:commons-lang3:3.21.0 \
	org.slf4j:slf4j-api:2.0.17
write_pom maven-compat \
	org.apache.maven:maven-model:%{version} \
	org.apache.maven:maven-model-builder:%{version} \
	org.apache.maven:maven-settings:%{version} \
	org.apache.maven:maven-settings-builder:%{version} \
	org.apache.maven:maven-artifact:%{version} \
	org.apache.maven:maven-core:%{version} \
	org.apache.maven:maven-resolver-provider:%{version} \
	org.apache.maven:maven-repository-metadata:%{version} \
	org.apache.maven.resolver:maven-resolver-api:1.9.16 \
	org.apache.maven.resolver:maven-resolver-util:1.9.16 \
	org.apache.maven.resolver:maven-resolver-impl:1.9.16 \
	org.codehaus.plexus:plexus-utils:3.6.2 \
	org.codehaus.plexus:plexus-interpolation:1.26 \
	org.eclipse.sisu:org.eclipse.sisu.plexus:0.3.5 \
	org.codehaus.plexus:plexus-component-annotations:2.2.0 \
	org.apache.maven.wagon:wagon-provider-api:3.5.3

%install
set -eo pipefail
: > .mfiles
install_one() {
	art="$1"
	sysjar install --buildroot %{buildroot} \
		--artifact "$art.pom:$art.jar" \
		--file-name "$art-%{version}" \
		--filelist ".mfiles-$art"
	/bin/mv "%{buildroot}/usr/share/sysjar/index/org.apache.maven/$art.sysjar" \
		"%{buildroot}/usr/share/sysjar/index/org.apache.maven/$art-%{version}.sysjar"
	sed -i "s|$art\\.sysjar|$art-%{version}.sysjar|" ".mfiles-$art"
	grep -F -q "\"version\": \"%{version}\"" "%{buildroot}/usr/share/sysjar/index/org.apache.maven/$art-%{version}.sysjar"
	test ! -e "%{buildroot}/usr/share/sysjar/index/org.apache.maven/$art.sysjar"
	while IFS= read -r line; do
		grep -qxF -- "$line" .mfiles || printf '%s\n' "$line" >> .mfiles
	done < ".mfiles-$art"
}
install_one maven-builder-support
install_one maven-artifact
install_one maven-model
install_one maven-repository-metadata
install_one maven-settings
install_one maven-plugin-api
install_one maven-model-builder
install_one maven-settings-builder
install_one maven-resolver-provider
install_one maven-core
install_one maven-compat

%check
set -eo pipefail
export JAVA_HOME=%{_jvmdir}/java-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
J=%{_javadir}
B=%{buildroot}$J
CP="$B/maven-model-%{version}.jar:$B/maven-artifact-%{version}.jar:$B/maven-builder-support-%{version}.jar"
CP="$CP:$B/maven-plugin-api-%{version}.jar:$B/maven-repository-metadata-%{version}.jar:$B/maven-settings-%{version}.jar"
CP="$CP:$B/maven-model-builder-%{version}.jar:$B/maven-settings-builder-%{version}.jar"
CP="$CP:$B/maven-resolver-provider-%{version}.jar:$B/maven-core-%{version}.jar:$B/maven-compat-%{version}.jar"
CP="$CP:$J/maven-resolver-api-1.9.16.jar:$J/maven-resolver-spi-1.9.16.jar:$J/maven-resolver-util-1.9.16.jar"
CP="$CP:$J/maven-resolver-impl-1.9.16.jar:$J/maven-resolver-named-locks-1.9.16.jar"
CP="$CP:$J/plexus-utils.jar:$J/plexus-xml.jar:$J/commons-lang3.jar:$J/plexus-interpolation-1.26.jar:$J/atinject.jar"
CP="$CP:$J/org.eclipse.sisu.inject-0.3.5.jar:$J/org.eclipse.sisu.plexus-0.3.5.jar"
CP="$CP:$J/plexus/plexus-sec-dispatcher.jar:$J/plexus-cipher.jar:$J/plexus-classworlds-2.7.0.jar"
CP="$CP:$J/maven-wagon/provider-api.jar:$J/slf4j-api.jar:$J/google-guice.jar:$J/guava.jar:$J/failureaccess.jar"
CP="$CP:$J/aopalliance.jar:$J/plexus-containers/plexus-component-annotations.jar:$J/maven-shared-utils.jar"
for jar in \
	"$B/maven-model-%{version}.jar" \
	"$B/maven-artifact-%{version}.jar" \
	"$B/maven-builder-support-%{version}.jar" \
	"$B/maven-plugin-api-%{version}.jar" \
	"$B/maven-repository-metadata-%{version}.jar" \
	"$B/maven-settings-%{version}.jar" \
	"$B/maven-model-builder-%{version}.jar" \
	"$B/maven-settings-builder-%{version}.jar" \
	"$B/maven-resolver-provider-%{version}.jar" \
	"$B/maven-core-%{version}.jar" \
	"$B/maven-compat-%{version}.jar"
do
	test -s "$jar"
done
mkdir -p check
cat > check/Smoke.java << 'END'
import java.io.File;
import java.io.StringReader;
import org.apache.maven.artifact.DefaultArtifact;
import org.apache.maven.artifact.handler.DefaultArtifactHandler;
import org.apache.maven.artifact.repository.metadata.Metadata;
import org.apache.maven.artifact.repository.metadata.io.xpp3.MetadataXpp3Reader;
import org.apache.maven.artifact.versioning.ComparableVersion;
import org.apache.maven.building.StringSource;
import org.apache.maven.model.Model;
import org.apache.maven.model.building.DefaultModelBuildingRequest;
import org.apache.maven.model.io.xpp3.MavenXpp3Reader;
import org.apache.maven.plugin.lifecycle.LifecycleConfiguration;
import org.apache.maven.plugin.lifecycle.io.xpp3.LifecycleMappingsXpp3Reader;
import org.apache.maven.profiles.ProfilesRoot;
import org.apache.maven.profiles.io.xpp3.ProfilesXpp3Reader;
import org.apache.maven.project.MavenProject;
import org.apache.maven.repository.internal.MavenRepositorySystemUtils;
import org.apache.maven.settings.Settings;
import org.apache.maven.settings.building.DefaultSettingsBuildingRequest;
import org.apache.maven.settings.io.xpp3.SettingsXpp3Reader;
import org.apache.maven.toolchain.model.PersistedToolchains;
import org.apache.maven.toolchain.model.io.xpp3.MavenToolchainsXpp3Reader;
import org.eclipse.aether.DefaultRepositorySystemSession;

public class Smoke {
	public static void main(String[] args) throws Exception {
		Model model = new MavenXpp3Reader().read(new StringReader(
			"<project><modelVersion>4.0.0</modelVersion><groupId>org.gradle</groupId><artifactId>gradle</artifactId><version>9.9.1</version></project>"));
		MavenProject project = new MavenProject(model);
		DefaultArtifact artifact = new DefaultArtifact("org.gradle", "gradle", "9.9.1", null, "jar", "", new DefaultArtifactHandler("jar"));
		ComparableVersion version = new ComparableVersion("3.9.5");
		StringSource source = new StringSource(model.getArtifactId());
		DefaultModelBuildingRequest request = new DefaultModelBuildingRequest().setValidationLevel(30);
		Settings settings = new SettingsXpp3Reader().read(new StringReader("<settings><offline>true</offline></settings>"));
		DefaultSettingsBuildingRequest settingsRequest = new DefaultSettingsBuildingRequest();
		settingsRequest.setUserSettingsFile(new File("settings.xml"));
		Metadata metadata = new MetadataXpp3Reader().read(new StringReader(
			"<metadata><groupId>org.gradle</groupId><artifactId>gradle</artifactId><version>9.9.1</version></metadata>"));
		LifecycleConfiguration lifecycles = new LifecycleMappingsXpp3Reader().read(new StringReader("<lifecycles/>"));
		ProfilesRoot profiles = new ProfilesXpp3Reader().read(new StringReader("<profilesXml/>"));
		PersistedToolchains toolchains = new MavenToolchainsXpp3Reader().read(new StringReader("<toolchains/>"));
		DefaultRepositorySystemSession session = MavenRepositorySystemUtils.newSession();
		int life = lifecycles.getLifecycles() == null ? 0 : lifecycles.getLifecycles().size();
		int prof = profiles.getProfiles() == null ? 0 : profiles.getProfiles().size();
		int tools = toolchains.getToolchains() == null ? 0 : toolchains.getToolchains().size();
		System.out.println("maven395_ok " + project.getArtifactId() + " " + artifact.getVersion()
			+ " " + version.getCanonical() + " " + source.getContent()
			+ " " + request.getValidationLevel() + " " + settings.isOffline()
			+ " " + settingsRequest.getUserSettingsFile().getName()
			+ " " + metadata.getArtifactId() + " " + life
			+ " " + prof + " " + tools
			+ " " + session.getClass().getSimpleName());
	}
}
END
javac --release 8 -encoding UTF-8 -Xlint:-options -proc:none -cp "$CP" -d check check/Smoke.java
java -cp "check:$CP" Smoke > check/out.txt
cat check/out.txt
grep -F -q 'maven395_ok gradle 9.9.1 3.9.5 gradle 30 true settings.xml gradle 0 0 0 DefaultRepositorySystemSession' check/out.txt

%files -f .mfiles
%doc LICENSE NOTICE
