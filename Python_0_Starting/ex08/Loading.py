import time
import sys

def ft_tqdm(lst: range) -> None:

    total = len(lst)
    start_time = time.time()
    
    for i, item in enumerate(lst):
        elapsed_time = time.time() - start_time
        progress = (i + 1) / total
        eta = (elapsed_time / progress) - elapsed_time if progress < 1 else 0
        it_per_sec = (i + 1) / elapsed_time if elapsed_time > 0 else 0

        # Ajuste da barra de progresso para incluir o espaço no meio
        bar_length = 50  
        half_length = bar_length // 2  # Metade da barra para inserir o espaço
        bar = '=' * half_length + ' ' + '=' * (half_length - 1) + '>'

        # Formatação dos tempos em [00:01<00:00] e garantindo dois dígitos para minutos/segundos
        elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed_time))
        eta_str = time.strftime("%M:%S", time.gmtime(eta))

        # Formatação da taxa de iterações por segundo com vírgula ao invés de ponto
        it_per_sec_str = f"{it_per_sec:,.2f}".replace('.', ',')

        # Exibição formatada no estilo solicitado
        sys.stdout.write(f"\r100%|[{bar}] {i + 1}/{total} {int(progress * 100):3}% | {i + 1}/{total}")
        sys.stdout.write(f" [{elapsed_str}<{eta_str}, {it_per_sec_str}it/s] ")
        sys.stdout.flush()  # Força a atualização imediata no terminal
        
        yield item

