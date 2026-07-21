# Polska 2040 — landing page

Konferencyjny landing page programu Polska 2040 w kierunku wizualnym „Suwerenne Skrzydło”.

## Lokalny podgląd

```bash
docker build -t polska2040-landing .
docker run --rm -p 8080:80 polska2040-landing
```

## K3s

Manifest korzysta z oficjalnego obrazu nginx i publicznego repozytorium. Kontener inicjalizacyjny pobiera zatwierdzony stan `main` przy starcie podu, dzięki czemu dokumenty nie muszą być pakowane do ograniczonej rozmiarem ConfigMapy. Nowe wydanie jest publikowane przez kontrolowany rollout po przejściu walidacji. Zastosowanie z katalogu `landingpage`:

```bash
kubectl apply -k .
kubectl -n polska2040 rollout status deployment/polska2040-landing
```

TLS jest obsługiwany przez Traefik. Manifest zakłada działający cert-manager i `ClusterIssuer` o nazwie `letsencrypt-prod`. Jeżeli klaster używa innego mechanizmu TLS, usuń adnotację cert-managera lub zmień nazwę wystawcy.
