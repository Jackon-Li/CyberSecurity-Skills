# 23 · 容器安全

[← 仓库首页](../README.md) · 分类 **23** · `ContainerSecurity` · **33** 个技能 · 领域 **蓝队**

> 每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。
> 技能内容**转载自上游开源项目，非原创**，版权归原作者所有。详见[来源与版权](../README.md#来源与版权)与[使用边界](../SECURITY.md)。

| # | 技能 | 英文标识 | 摘要 | 入口 |
|---|---|---|---|---|
| 1 | **Calico容器网络策略** | `implementing-container-network-policies-with-calico` | Uses Calico's own policy CRDs beyond the upstream Kubernetes API - Glo… | [SKILL.md](skills/Calico容器网络策略_implementing-container-network-policies-with-calico/SKILL.md) |
| 2 | **Calico网络策略实施** | `implementing-kubernetes-network-policy-with-calico` | Installs Calico as the cluster CNI and writes standard Kubernetes Netw… | [SKILL.md](skills/Calico网络策略实施_implementing-kubernetes-network-policy-with-calico/SKILL.md) |
| 3 | **Cosign镜像签名验证** | `implementing-image-provenance-verification-with-cosign` | Signs and verifies container image provenance with Sigstore Cosign, co… | [SKILL.md](skills/Cosign镜像签名验证_implementing-image-provenance-verification-with-cosign/SKILL.md) |
| 4 | **Docker Bench安全评估** | `performing-docker-bench-security-assessment` | Runs Docker Bench for Security, the open-source CIS Docker Benchmark a… | [SKILL.md](skills/Docker%20Bench安全评估_performing-docker-bench-security-assessment/SKILL.md) |
| 5 | **Docker守护进程加固** | `hardening-docker-daemon-configuration` | Hardens the Docker daemon (dockerd) through /etc/docker/daemon.json wi… | [SKILL.md](skills/Docker守护进程加固_hardening-docker-daemon-configuration/SKILL.md) |
| 6 | **Docker容器生产加固** | `hardening-docker-containers-for-production` | Hardens Dockerfiles, images, and per-container runtime settings agains… | [SKILL.md](skills/Docker容器生产加固_hardening-docker-containers-for-production/SKILL.md) |
| 7 | **Falco容器运行时防护** | `detecting-container-runtime-threats-with-falco` | Deploys and operates Falco with the modern eBPF driver in Kubernetes a… | [SKILL.md](skills/Falco容器运行时防护_detecting-container-runtime-threats-with-falco/SKILL.md) |
| 8 | **Falco逃逸规则编写** | `detecting-container-escape-with-falco-rules` | Writes and tunes Falco rule syntax for container escape detection - co… | [SKILL.md](skills/Falco逃逸规则编写_detecting-container-escape-with-falco-rules/SKILL.md) |
| 9 | **Grype镜像漏洞扫描** | `scanning-container-images-with-grype` | Scans container images, filesystems, and SBOMs for known CVEs with Anc… | [SKILL.md](skills/Grype镜像漏洞扫描_scanning-container-images-with-grype/SKILL.md) |
| 10 | **Harbor镜像仓库加固** | `securing-container-registry-with-harbor` | Configures the security features of the Harbor open-source container r… | [SKILL.md](skills/Harbor镜像仓库加固_securing-container-registry-with-harbor/SKILL.md) |
| 11 | **Helm部署安全加固** | `securing-helm-chart-deployments` | Secures Helm chart deployments by verifying chart signatures and prove… | [SKILL.md](skills/Helm部署安全加固_securing-helm-chart-deployments/SKILL.md) |
| 12 | **K8s CIS基准审计** | `performing-kubernetes-cis-benchmark-with-kube-bench` | Turns kube-bench output into a finished CIS Kubernetes Benchmark audit… | [SKILL.md](skills/K8s%20CIS基准审计_performing-kubernetes-cis-benchmark-with-kube-bench/SKILL.md) |
| 13 | **K8s Pod安全标准** | `implementing-kubernetes-pod-security-standards` | Chooses and applies the correct Kubernetes Pod Security Standard (Priv… | [SKILL.md](skills/K8s%20Pod安全标准_implementing-kubernetes-pod-security-standards/SKILL.md) |
| 14 | **K8s Pod提权检测** | `detecting-privilege-escalation-in-kubernetes-pods` | Detects and prevents privilege escalation inside Kubernetes pods by co… | [SKILL.md](skills/K8s%20Pod提权检测_detecting-privilege-escalation-in-kubernetes-pods/SKILL.md) |
| 15 | **K8s RBAC加固** | `implementing-rbac-hardening-for-kubernetes` | Hardens Kubernetes RBAC by designing least-privilege Roles and Cluster… | [SKILL.md](skills/K8s%20RBAC加固_implementing-rbac-hardening-for-kubernetes/SKILL.md) |
| 16 | **K8s RBAC提权审计** | `auditing-kubernetes-rbac-privilege-escalation` | Finds over-permissive RBAC roles and service-account token abuse paths… | [SKILL.md](skills/K8s%20RBAC提权审计_auditing-kubernetes-rbac-privilege-escalation/SKILL.md) |
| 17 | **K8s审计日志分析** | `analyzing-kubernetes-audit-logs` | Parses Kubernetes API server audit logs (JSON lines) to detect exec-in… | [SKILL.md](skills/K8s审计日志分析_analyzing-kubernetes-audit-logs/SKILL.md) |
| 18 | **K8s渗透测试** | `performing-kubernetes-penetration-testing` | Evaluates Kubernetes cluster security by actively simulating attacker… | [SKILL.md](skills/K8s渗透测试_performing-kubernetes-penetration-testing/SKILL.md) |
| 19 | **K8s网络策略实施** | `implementing-network-policies-for-kubernetes` | Writes portable upstream Kubernetes NetworkPolicy YAML - default-deny-… | [SKILL.md](skills/K8s网络策略实施_implementing-network-policies-for-kubernetes/SKILL.md) |
| 20 | **Kubesec清单扫描** | `scanning-kubernetes-manifests-with-kubesec` | Scores Kubernetes resource manifests with Kubesec to flag misconfigura… | [SKILL.md](skills/Kubesec清单扫描_scanning-kubernetes-manifests-with-kubesec/SKILL.md) |
| 21 | **OPA Gatekeeper策略执行** | `implementing-opa-gatekeeper-for-policy-enforcement` | Deploys OPA Gatekeeper via Helm as a Kubernetes admission controller a… | [SKILL.md](skills/OPA%20Gatekeeper策略执行_implementing-opa-gatekeeper-for-policy-enforcement/SKILL.md) |
| 22 | **Pod安全准入控制器** | `implementing-pod-security-admission-controller` | Configures and operates the Kubernetes Pod Security Admission (PSA) co… | [SKILL.md](skills/Pod安全准入控制器_implementing-pod-security-admission-controller/SKILL.md) |
| 23 | **Tetragon运行时安全** | `implementing-runtime-security-with-tetragon` | Implements eBPF-based runtime observability and in-kernel enforcement… | [SKILL.md](skills/Tetragon运行时安全_implementing-runtime-security-with-tetragon/SKILL.md) |
| 24 | **Trivy容器安全扫描** | `performing-container-security-scanning-with-trivy` | Runs Trivy across every target type it supports - container images, fi… | [SKILL.md](skills/Trivy容器安全扫描_performing-container-security-scanning-with-trivy/SKILL.md) |
| 25 | **Trivy镜像扫描** | `scanning-docker-images-with-trivy` | Scans a Docker image with Trivy for vulnerabilities in OS packages and… | [SKILL.md](skills/Trivy镜像扫描_scanning-docker-images-with-trivy/SKILL.md) |
| 26 | **distroless精简镜像** | `implementing-container-image-minimal-base-with-distroless` | Reduces container attack surface by building application images on Goo… | [SKILL.md](skills/distroless精简镜像_implementing-container-image-minimal-base-with-distroless/SKILL.md) |
| 27 | **etcd安全评估** | `performing-kubernetes-etcd-security-assessment` | Assesses the security posture of the etcd cluster backing Kubernetes:… | [SKILL.md](skills/etcd安全评估_performing-kubernetes-etcd-security-assessment/SKILL.md) |
| 28 | **in-toto供应链安全** | `implementing-supply-chain-security-with-in-toto` | Implements supply chain integrity verification for container builds wi… | [SKILL.md](skills/in-toto供应链安全_implementing-supply-chain-security-with-in-toto/SKILL.md) |
| 29 | **kube-bench基准检查** | `benchmarking-kubernetes-with-kube-bench` | Installs and runs the kube-bench tool against a Kubernetes cluster as… | [SKILL.md](skills/kube-bench基准检查_benchmarking-kubernetes-with-kube-bench/SKILL.md) |
| 30 | **容器运行时漂移检测** | `detecting-container-drift-at-runtime` | Detects unauthorized runtime drift in containers by monitoring binary… | [SKILL.md](skills/容器运行时漂移检测_detecting-container-drift-at-runtime/SKILL.md) |
| 31 | **容器逃逸到宿主机** | `escaping-containers-to-host` | Exploits privileged pods, host mounts, runC CVEs, and exposed Docker s… | [SKILL.md](skills/容器逃逸到宿主机_escaping-containers-to-host/SKILL.md) |
| 32 | **容器逃逸尝试检测** | `detecting-container-escape-attempts` | Detects container escape at runtime across tooling - namespace manipul… | [SKILL.md](skills/容器逃逸尝试检测_detecting-container-escape-attempts/SKILL.md) |
| 33 | **容器逃逸配置审计** | `performing-container-escape-detection` | Audits container and pod configuration for escape-enabling misconfigur… | [SKILL.md](skills/容器逃逸配置审计_performing-container-escape-detection/SKILL.md) |

---

<sub>本页由脚本生成 · 技能内容转载自上游项目，非原创 · [返回首页](../README.md) · [索引](../index.json) · [使用边界](../SECURITY.md)</sub>
