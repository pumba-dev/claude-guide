<#
    Exporta um .pptx para .pdf usando o PowerPoint instalado, via COM.

    Uso:
        powershell -ExecutionPolicy Bypass -File slides/scripts/exportar_pdf.ps1 -Pptx <caminho> [-Pdf <caminho>]

    O PDF é o artefato de conferência: permite revisar o deck página a página
    e validar o resultado sem abrir o PowerPoint.

    A conversão trabalha sobre uma cópia temporária. Sem isso, se o arquivo
    estiver aberto na tela do apresentador, o COM fica travado esperando um
    diálogo de arquivo em uso que ninguém vê.
#>

param(
    [Parameter(Mandatory = $true)][string]$Pptx,
    [string]$Pdf
)

$ErrorActionPreference = "Stop"

$Pptx = (Resolve-Path -LiteralPath $Pptx).Path
if (-not $Pdf) { $Pdf = [System.IO.Path]::ChangeExtension($Pptx, ".pdf") }

$dirPdf = Split-Path -Parent $Pdf
if ($dirPdf -and -not (Test-Path $dirPdf)) { New-Item -ItemType Directory -Path $dirPdf | Out-Null }
if (-not [System.IO.Path]::IsPathRooted($Pdf)) { $Pdf = Join-Path (Get-Location).Path $Pdf }

$temp = Join-Path $env:TEMP ("deck-" + [Guid]::NewGuid().ToString("N") + ".pptx")
Copy-Item -LiteralPath $Pptx -Destination $temp -Force

$ppSaveAsPDF = 32
$msoFalse = 0
$msoTrue = -1
$app = $null
$apresentacao = $null

try {
    # O PowerPoint recusa chamadas COM enquanto está ocupado ou com diálogo
    # aberto (RPC_E_CALL_REJECTED). Algumas tentativas resolvem; se o
    # apresentador estiver com o arquivo aberto na tela, feche e repita.
    for ($tentativa = 1; $tentativa -le 5; $tentativa++) {
        try {
            $app = New-Object -ComObject PowerPoint.Application
            break
        }
        catch {
            if ($tentativa -eq 5) {
                throw "PowerPoint não respondeu ao COM após 5 tentativas. Feche o PowerPoint e repita. Detalhe: $($_.Exception.Message)"
            }
            Start-Sleep -Seconds 3
        }
    }
    $app.DisplayAlerts = 1  # ppAlertsNone
    # Open(FileName, ReadOnly, Untitled, WithWindow)
    $apresentacao = $app.Presentations.Open($temp, $msoTrue, $msoFalse, $msoFalse)
    $apresentacao.SaveAs($Pdf, $ppSaveAsPDF)
    Write-Output "PDF gerado: $Pdf"
}
finally {
    if ($apresentacao) { try { $apresentacao.Close() } catch {} }
    if ($app) { try { $app.Quit() } catch {} }
    if ($apresentacao) { [void][Runtime.InteropServices.Marshal]::ReleaseComObject($apresentacao) }
    if ($app) { [void][Runtime.InteropServices.Marshal]::ReleaseComObject($app) }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
    Remove-Item -LiteralPath $temp -Force -ErrorAction SilentlyContinue
}
