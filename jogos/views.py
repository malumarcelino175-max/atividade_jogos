from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Desenvolvedora, Jogo, Plataforma


def lista_jogos(request):
    q = request.GET.get("q", "").strip()
    desenvolvedora_id = request.GET.get("desenvolvedora", "").strip()
    plataforma_id = request.GET.get("plataforma", "").strip()

    # Consulta ORM trazendo os modelos relacionados (Desenvolvedora e Plataforma)
    queryset = Jogo.objects.select_related("desenvolvedora", "plataforma").all()

    # RF04: Pesquisa textual pelo nome do jogo (case-insensitive)
    if q:
        queryset = queryset.filter(nome__icontains=q)

    # RF05: Filtros dinâmicos pelos relacionamentos via GET
    if desenvolvedora_id:
        queryset = queryset.filter(desenvolvedora_id=desenvolvedora_id)

    if plataforma_id:
        queryset = queryset.filter(plataforma_id=plataforma_id)

    # RF06: Paginação com 5 registros por página (sempre após os filtros)
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # RF07: Preserva os filtros ativos ao navegar entre as páginas
    params = request.GET.copy()
    params.pop("page", None)
    querystring = params.urlencode()

    context = {
        "page_obj": page_obj,
        "desenvolvedoras": Desenvolvedora.objects.all(),
        "plataformas": Plataforma.objects.all(),
        "q": q,
        "desenvolvedora_selecionada": desenvolvedora_id,
        "plataforma_selecionada": plataforma_id,
        "querystring": querystring,
        "total_resultados": paginator.count,
    }
    return render(request, "jogos/lista_jogos.html", context)
